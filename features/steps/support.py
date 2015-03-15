import inspect
from behave import *
from goat.matcher import GoatMatcher

use_step_matcher("re")


@step("Create pattern: (.*)")
def create_pattern(context, pattern: str):
    context.pattern = pattern


@step("Create function: (.*)")
def create_function(context, function: str):
    index = function.index("(")
    exec("def f{}: pass".format(function[index:]))
    exec("context.function = f")


@step("Assert result is: (.*)")
def assert_result_is(context, expected_result: str):
    assert context.result == expected_result, "{} was expected, result was: {}".format(expected_result,
                                                                                          context.result)


@step("Assert context parameters are: (.*)")
def assert_context_parameters_are(context, expected_result: str):
    expected_result = expected_result.split(" ")
    assert context.context_params == expected_result, "{} was expected, result was: {}".format(expected_result,
                                                                                          context.context_params)


@step("Convert pattern to cfparse")
def convert_pattern(context):
    class GoatMatcherMock(GoatMatcher):
        def __init__(self, func, pattern, step_type=None):
            self.context_params = []
            self.signature = inspect.signature(func)

    matcher = GoatMatcherMock(context.function, context.pattern)
    context.result = matcher.convert(context.function, context.pattern)
    context.context_params = matcher.context_params