import inspect
from goat import string
from collections import OrderedDict

from behave import matchers

try:
    from behave.model import Argument as Argument_
    from behave.model import Match as Match_
except ImportError:
    from behave.model_core import Argument as Argument_
    from behave.matchers import Match as Match_

from parse_type import cfparse

from goat import model
from goat.types import TYPE_TO_PARSE_TYPE_MAP


class GoatFormatter(string.Formatter):
    def __init__(self):
        self.unused_args = []

    def check_unused_args(self, used_args, args: tuple, kwargs: OrderedDict):
        kwarg_key_list = list(kwargs.keys())

        for used_arg in used_args:
            if isinstance(used_arg, int):
                key = kwarg_key_list[used_arg]
            else:
                key = used_arg
            kwargs.pop(key)

        self.unused_args = list(kwargs.keys())


class GoatMatcher(matchers.CFParseMatcher):
    def __init__(self, func, pattern, step_type=None):
        matchers.Matcher.__init__(self, func, pattern, step_type)
        self.context_params = []
        self.signature = inspect.signature(func)

        pattern = self.convert(pattern)
        self.parser = cfparse.Parser(pattern, self.custom_types)

    def match(self, step) -> Match_:
        result = self.check_match(step)
        if result is None:
            return None
        return model.Match(self.func, self.signature, result)

    def check_match(self, step) -> list:
        """Like matchers.CFParseMatcher.check_match but
        also add the implicit parameters from the context
        """
        args = []
        match = super().check_match(step)
        if match is None:
            return None

        for arg in match:
            args.append(model.Argument.from_argument(arg))

        for arg in self.context_params:
            args.append(model.Argument(0, 0, "", None, name=arg, implicit=True))

        return args

    def convert_type_to_parse_type(self, parameter):
        annotation = parameter.annotation
        if not isinstance(annotation, str):
            annotation = annotation.__name__
        annotation = TYPE_TO_PARSE_TYPE_MAP.get(annotation, annotation)
        return annotation

    def convert(self, pattern: str) -> str:
        """Convert the goat step string to CFParse String"""
        parameters = OrderedDict()
        for parameter in self.signature.parameters.values():
            annotation = self.convert_type_to_parse_type(parameter)
            parameters[parameter.name] = "{%s:%s}" % (parameter.name, annotation)

        formatter = GoatFormatter()

        # We have to use vformat here to ensure that kwargs will be OrderedDict
        values = parameters.values()
        parameter_list = list(values)
        converted_pattern = formatter.vformat(pattern, parameter_list, parameters)

        self.context_params = formatter.unused_args
        return converted_pattern