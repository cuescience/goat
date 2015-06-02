![Goat](https://cloud.githubusercontent.com/assets/831374/7931713/d42b7f4a-090a-11e5-8b74-c96391a9503b.png)


Goat implements a matcher for [behave](https://github.com/behave/behave) wich uses python3 function annotations for specifiying parameter types in step definitions.

```python
@given("my name is {name} and I'm {age} years old")
def my_name_and_age(name: str, age: int) -> Person:
    pass
```

## Installation
```
pip install goat
```

## Getting started
If you are not familiar with behave, you can get started by reading the [tutorial](http://pythonhosted.org/behave/tutorial.html).


To start using goat you have to register the GoatMatcher:
```python
from behave import *
from behave import matchers
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
The indexes of the placeholders has to correspond to the order of the function arguments.

### Types
Following standard types are available by now: int, float, str. Behave types like Table, Context, Text are also supported.
If this is not enough, you can easily extend it (e.g. goat.types.Word):
```python
import parse
from behave import register_type

@parse.with_pattern(r"\w+")
def parse_word(value: str) -> Word:
    return Word(value)


register_type(Word=parse_word)
```

**Feel free to submit a Pull Request if you think the type extension is useful for others!**

### Implicit parameters
As mentioned before, there is no need to add *context* as first argument in your step definitions. But how you then pass state from one step to another? With the help of **Implicit parameters** your step definitions will become much cleaner.

If you want to add some value to the context just return it in your step definition (make sure to also add a return function annotation):
```python
@given("my name is {name} and I'm {age} years old")
def my_name_and_age(name: str, age: int) -> Person:
    return Person(name, age)

@then("assert the given person is {} years old")
def assert_person_is_n_years_old(expected_age: int, person: Person):
    assert person.age == expected_age
```

If you make use of the sentences in a feature file the returned Person of the *my_name_and_age* step will be passed into the *assert_person_is_n_years_old* step.
```gherkin
Feature: Test
Scenario: Implicit parameters

Given my name is Ilja and I'm 24 years old
Then assert the given person is 24 years old
```

You can also use behaves Table and Text like this:
```python
from behave.model import Table, Text

@given("folowing table:")
def given_following_table(table: Table):
    pass
    
@given("folowing text:")
def given_following_text(text: Text):
    pass
```

If you really need the whole context or you want to migrate your old behave test suite, you can also pass the context explicitly:
```python
from behave.runner import Context

@given("Assert context contains a person with age {}")
def assert_context_contains(age: int, context: Context):
    pass
```
