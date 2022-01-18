Feature: ISBN
  Scenario Outline: ISBN
    Given ISBN validate function
    When the inputed number is  <num>
	Then the output is <result>
		Examples:
			| num 			| result |
			| 978-3-16-148410-0 | True |
            | 978-0-306-40615-7 | True |
             |  978-3-16-148410 | False |
    |978-7654-321-122-4 | False|
 |977-7654-321-12-4 | False |
    | 978-7654-321-1-41 | False|
    | 979-11111-11-11-2 | True |
    | 978-7654-321-12-4 | False |
 |977-7654-321-12-4 | False|
