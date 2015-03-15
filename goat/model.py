import inspect
from typing import *
from behave import model

CONTEXT_NAMESPACE = "_goat_{}"


class Argument(model.Argument):
    def __init__(self, *args, **kwargs):
        self.implicit = kwargs.pop("implicit", False)
        super().__init__(*args, **kwargs)

    @staticmethod
    def from_argument(argument: model.Argument, implicit=False):
        return Argument(
            argument.start,
            argument.end,
            argument.original,
            argument.value,
            name=argument.name,
            implicit=implicit
        )


class Match(model.Match):
    def __init__(self, func, signature, arguments: List[Argument]=None):
        self.signature = signature
        super().__init__(func, arguments)

    @property
    def explicit_arguments(self):
        return filter(lambda x: not x.implicit, self.arguments)

    @property
    def implicit_arguments(self):
        return filter(lambda x: x.implicit, self.arguments)

    def run(self, context):
        """We have to overwrite this method because we don't want an implicit context
        """

        args = []
        kwargs = {}
        for arg in self.explicit_arguments:
            if arg.name is not None:
                kwargs[arg.name] = arg.value
            else:
                args.append(arg.value)

        for arg in self.implicit_arguments:
            if arg.name is not None:
                annotation = self.signature.parameters[arg.name].annotation
                if not isinstance(annotation, str):
                    annotation = annotation.__name__

                value = context.__getattr__(CONTEXT_NAMESPACE.format(annotation))

                kwargs[arg.name] = value
            else:
                raise RuntimeError("Argument name shouldn't be None")

        with context.user_mode():
            return_value = self.func(*args, **kwargs)
            return_annotation = self.signature.return_annotation
            if return_annotation == inspect.Signature.empty:
                return

            if not isinstance(return_annotation, str):
                return_annotation = return_annotation.__name__

            context.__setattr__(CONTEXT_NAMESPACE.format(return_annotation), return_value)

    def get_implicit_parameters_from_context(self) -> list:
        pass