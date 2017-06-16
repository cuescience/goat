import inspect
from behave.model import Table, Text

try:
    from behave.model import Argument as Argument_
    from behave.model import Match as Match_
except ImportError:
    from behave.model_core import Argument as Argument_
    from behave.matchers import Match as Match_

from behave.runner import Context

CONTEXT_NAMESPACE = "_goat_{}"


class Argument(Argument_):
    def __init__(self, *args, implicit=False, **kwargs):
        self.implicit = implicit
        super().__init__(*args, **kwargs)

    @staticmethod
    def from_argument(argument: Argument_, implicit=False):
        return Argument(
            argument.start,
            argument.end,
            argument.original,
            argument.value,
            name=argument.name,
            implicit=implicit
        )


class Match(Match_):
    def __init__(self, func, signature, arguments: list = None):
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
                annotation_name = annotation
                if not isinstance(annotation, str):
                    annotation_name = annotation.__name__

                if annotation is Table:
                    value = context.table
                elif annotation is Context:
                    value = context
                elif annotation is Text:
                    value = context.text
                elif annotation is inspect._empty:
                    raise RuntimeError(
                        "Parameter '{}' of step implementation '{}{}' does not have a type! Please specify it in the correct steps file.".format(
                            arg.name,
                            self.func.__qualname__,
                            self.signature,

                        )
                    )
                elif CONTEXT_NAMESPACE.format(annotation_name) in context:
                    value = context.__getattr__(CONTEXT_NAMESPACE.format(annotation_name))
                else:
                    raise RuntimeError(
                        "'{}' was not found in context. Is a context parameter missing?".format(arg.name))

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
