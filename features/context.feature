Feature: Context parameters

  Scenario: Implicit indexed parameter
    * Create pattern: The result is {}
    * Create function: the_result_is(expected_result: int, result:int)
    * Convert pattern to cfparse
    * Assert context parameters are: result

  Scenario: Explicit indexed parameter, context parameter last
    * Create pattern: The result is {0}
    * Create function: the_result_is(expected_result: int, result:int)
    * Convert pattern to cfparse
    * Assert context parameters are: result

  Scenario: Explicit indexed parameter, context parameter first
    * Create pattern: The result is {1}
    * Create function: the_result_is(result:int, expected_result: int)
    * Convert pattern to cfparse
    * Assert context parameters are: result

  Scenario: Named parameter, context parameter last
    * Create pattern: The result is {expected_result}
    * Create function: the_result_is(expected_result: int, result:int)
    * Convert pattern to cfparse
    * Assert context parameters are: result

  Scenario: Named parameter, context parameter first
    * Create pattern: The result is {expected_result}
    * Create function: the_result_is(result:int, expected_result: int)
    * Convert pattern to cfparse
    * Assert context parameters are: result

  Scenario: Mixed parameter
    * Create pattern: The result is {expected_result} with variance {1}
    * Create function: the_result_is(result:int, variance:int, expected_result: int)
    * Convert pattern to cfparse
    * Assert context parameters are: result

  Scenario: Error that raises when a parameter is not in the context but is expected
    * Create function: pattern_with_expected_but_missing_context_parameter(context_parameter: str)
    * Expect RuntimeError with message 'context_parameter' was not found in context. Is a context parameter missing?
    * Run function with arguments
      | Argument          | Value | Implicit |
      | context_parameter |       | True     |