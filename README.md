![Goat](https://cloud.githubusercontent.com/assets/831374/7931713/d42b7f4a-090a-11e5-8b74-c96391a9503b.png)

Goat implements a matcher for [behave](https://github.com/behave/behave) wich uses python3 function annotations for specifiying parameter types in step definitions.

```python
@given("My name is {name} and I'm {age} years old")
def my_name_and_age(name: str, age: int) -> Person:
    ...
```

## Installation
```
pip install goat
```
