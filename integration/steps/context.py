from behave import *
from behave import matchers
from behave.model import Table, Text
from behave.runner import Context
from goat import types
from goat.matcher import GoatMatcher

matchers.matcher_mapping.update({"goat": GoatMatcher})
use_step_matcher("goat")


@step("This function returns {}")
def this_function_returns(a: int) -> int:
    return 5


@step("This argless function returns 5")
def this_argless_function_returns() -> int:
    return 5


@step("This function returns {} and takes a Table")
def this_function_takes_a_table(p: int, table: Table):
    assert isinstance(p, int)
    assert isinstance(table, Table)
    assert len(table.rows) == 1
    return p


@step("This function returns {} and needs Text")
def this_function_takes_a_table(p: int, text: Text):
    assert isinstance(p, int)
    assert isinstance(text, Text)
    assert text == "This is the text provided"
    return p


@step("This function returns {} and needs the Context")
def this_function_takes_a_table(p: int, context: Context):
    assert isinstance(p, int)
    assert isinstance(context, Context)


@step("Assert that the result was {}")
def assert_that_the_result_was(expected_result: int, result: int) -> int:
    assert expected_result == result


