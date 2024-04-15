# Created by Victor Stankov at 30-Mar-2024
Feature: Data Input
    Scenario Outline: Incorrect Number of Independent Variables
    Given the app is started
    And the user has to enter the number of independent variables
    When the user enters <Wrong Input>
    Then the app displays an error and asks the user again to enter a value

    Examples:
      | Wrong Input        |
      | a non-number input |
      | number < 2         |

  Scenario: Incorrect Path for Input file
    Given the user has entered the number of independent variables
    When the user enters incorrect path
    Then the app displays an error and exits with exit code 1

Feature: Data reading:
    Scenario: Incorrect Data in Input file
    Given the user has entered a valid path for the input file
    When the file has a non-number element
    Then the app displays an error and exits with exit code 2

  Scenario: Incorrect Combination of Number of Independent Variables and Input file
    Given the user has entered the number of independent variables
    And the input file has been read
    When the number of independent variables does not match the number of columns in the input file - 1
    Then the app displays an error and exits with exit code 3

Feature: Find Regression Coefficients
  Scenario: All Checks Pass Through Successfully
    Given the user has entered a valid number of independent variables
    And the user has entered a valid path for the input file
    And the input file contains all valid numerical data
    And the number of independent variables matches the number of columns in the input file - 1
    When the app processes the input
    Then the app displays the coefficients to the user
