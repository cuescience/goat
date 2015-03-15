Feature: Parameters can be specified with explicit index e.g. {0}

  Scenario: Parameters in the order of function arguments
    * Create pattern: My name is {0} and I'm {1} years old
    * Create function: my_name_is(name: str, age:int)
    * Convert pattern to cfparse
    * Assert result is: My name is {name:str} and I'm {age:d} years old

  Scenario: Parameters in different order than function arguments
    * Create pattern: My name is {1} and I'm {0} years old
    * Create function: my_name_is(age:int, name: str)
    * Convert pattern to cfparse
    * Assert result is: My name is {name:str} and I'm {age:d} years old