from behave import *
from behave import matchers
from goat import types
from goat.matcher import GoatMatcher

matchers.matcher_mapping.update({"goat": GoatMatcher})
use_step_matcher("goat")


@step("This function returns {}")
def this_function_returns(a: int) -> int:
    return 5

@step("Assert that the result was {}")
def assert_that_the_result_was(expected_result: int, result: int) -> int:
    assert expected_result == result