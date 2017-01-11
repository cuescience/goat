Feature: Test errors

  Scenario: Error that raises when a parameter does not have a type
    * Create function: invalid_pattern_with_missing_parameter_type(test)
    * Expect RuntimeError with message Parameter 'test' of step implementation 'f(test)' does not have a type! Please specify it in the correct steps file.
    * Run function with arguments
      | Argument | Value | Implicit |
      | test     | 1     | True    |
