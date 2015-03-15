import parse
from behave import register_type

TYPE_TO_PARSE_TYPE_MAP = {
    "int": "d",
    "float": "f",
}


class Word(str):
    pass


@parse.with_pattern(r"(.*)")
def parse_str(value: str) -> str:
    return value


@parse.with_pattern(r"\w+")
def parse_word(value: str) -> Word:
    return Word(value)


register_type(str=parse_str, Word=parse_word)