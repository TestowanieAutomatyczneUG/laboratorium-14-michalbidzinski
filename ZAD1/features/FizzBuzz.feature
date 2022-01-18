Feature: FizzBuzz
  Scenario Outline: FizzBuzz
    Given FizzBuzz feature
    When I pass the  <num>
    Then The result is <output>
    Examples:
      | num | output   |
      | 3   | Fizz     |
      | 5   | Buzz     |
      | 15  | FizzBuzz |
      | 1   | 1        |
      | 4   | 4        |
      | 1025| Buzz    |
      | []  | err    |
      | {}  | err    |