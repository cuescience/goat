Feature: Parameters can be specified with name e.g. {name}
  Scenario: Parameters in the order of function arguments
    * Create pattern: My name is {name} and I'm {age} years old
    * Create function: my_name_is(name: str, age:int)
    * Convert pattern to cfparse
    * Assert result is: My name is {name:str} and I'm {age:int} years old

  Scenario: Order of function arguments doesn't matter
    * Create pattern: My name is {name} and I'm {age} years old
    * Create function: my_name_is(age:int, name: str)
    * Convert pattern to cfparse
    * Assert result is: My name is {name:str} and I'm {age:int} years old