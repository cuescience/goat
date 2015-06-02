![Goat](https://cloud.githubusercontent.com/assets/831374/7931713/d42b7f4a-090a-11e5-8b74-c96391a9503b.png)

Goat implements a matcher for [behave](https://github.com/behave/behave) wich uses python3 function annotations for specifiying parameter types in step definitions.

```python
@given("my name is {name} and I'm {age} years old")
def my_name_and_age(name: str, age: int) -> Person:
    ...
```

## Installation
```
pip install goat
```

## Getting started
If you are not familiar with behave, you can get started by reading the [tutorial](http://pythonhosted.org/behave/tutorial.html)


To start using goat you have to register the GoatMatcher:
```python
from goat.matcher import GoatMatcher

matchers.matcher_mapping.update({"goat": GoatMatcher})
use_step_matcher("goat")
```

Now you can specify you step definitions like this:
```python
@given("my name is {name} and I'm {age} years old")
def my_name_and_age(name: str, age: int) -> Person:
    ...
```
**Be aware that unlike other behave matchers there is no need to pass the context variable as first argument.**

The arguments will be of the right type:
```
>>> type(age)
<type 'int'>
>>> type(name)
<type 'str'>
```

Instead of using named placeholder you can also use unnamed and indexed ones:
```python
@given("my name is {} and I'm {} years old")
def my_name_and_age(name: str, age: int) -> Person:
```
```python
@given("my name is {0} and I'm {1} years old")
def my_name_and_age(name: str, age: int) -> Person:
```
The index of the placeholder has to correspond to the order of the function arguments.

### Types
Following standard types are available by now: int, float, str.
But you can easily extend it (e.g. goat.types.Word):
```python
import parse
from behave import register_type

@parse.with_pattern(r"\w+")
def parse_word(value: str) -> Word:
    return Word(value)


register_type(Word=parse_word)
```
