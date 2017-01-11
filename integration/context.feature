Feature: Context

  Scenario: Implicit parameters from context
    * This function returns 5
    * Assert that the result was 5

  Scenario: Implicit parameters from context without args
    * This argless function returns 5
    * Assert that the result was 5

  Scenario: Table as context parameter
    * This function returns 5 and takes a Table
      | Header 1 | Header 2 |
      | Row 1    | Row 2    |

  Scenario: Multi line text as context parameter
    * This function returns 5 and needs Text
    """
    This is the text provided
    """

  Scenario: The context itself as context parameter
    * This function returns 5 and needs the Context
