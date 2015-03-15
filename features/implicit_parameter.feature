Feature: Parameters can be specified by implicit index e.g. {}

  Scenario: Parameter are in the right order
    * Create pattern: My name is {} and I'm {} years old
    * Create function: my_name_is(name: str, age:int)
    * Convert pattern to cfparse
    * Assert result is: My name is {name:str} and I'm {age:d} years old

  Scenario: Function argument order change pattern
    * Create pattern: My name is {} and I'm {} years old
    * Create function: my_name_is(age:int, name: str)
    * Convert pattern to cfparse
    * Assert result is: My name is {age:d} and I'm {name:str} years old