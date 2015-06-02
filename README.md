![Goat](https://cloud.githubusercontent.com/assets/831374/7931635/2b49d3a4-090a-11e5-96b7-cd5365a6b6ee.png)

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
