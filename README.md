# goat
Goat implements a matcher for [behave](https://github.com/behave/behave) wich uses python3 function annotations for specifiying parameter types in steps.

```python
@given("My name is {name} and I'm {age} years old")
def my_name_and_age(name: str, age: int):
    pass
```

## Installation
```
pip install goat
```
