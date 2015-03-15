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
    assert context.result[1] == expected_result, "{} was expected, result was: {}".format(expected_result,
                                                                                          context.result[1])


@step("Convert pattern to cfparse")
def convert_pattern(context):
    class GoatMatcherMock(GoatMatcher):
        def __init__(self):
            pass

    context.result = GoatMatcherMock().convert(context.function, context.pattern)