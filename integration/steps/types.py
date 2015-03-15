from behave import *
from behave import matchers
from goat import types
from goat.matcher import GoatMatcher

matchers.matcher_mapping.update({"goat": GoatMatcher})
use_step_matcher("goat")


@step("{} is an integer")
def is_an_integer(a: int):
    assert_isinstance(a, int)


@step("{} is a float")
def is_a_float(a: float):
    assert_isinstance(a, float)


@step("\"{}\" is a string")
def is_a_string(words: str):
    assert_isinstance(words, str)


@step("{} is a word")
def is_an_word(word: types.Word):
    assert_isinstance(word, types.Word)


def assert_isinstance(value, expected_type):
    assert isinstance(value, expected_type), "Should be instanceof: {}, but was {}".format(expected_type, type(value))
