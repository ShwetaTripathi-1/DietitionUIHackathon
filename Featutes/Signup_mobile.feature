Feature: Dietician Website Sign up with email Page
Scenario: Validating the Sign Up form heading
    Given User is on Dietician website
    When User lands on Register page
    Then User should see a form with heading "Sign Up form", to sign up using mobile number

  Scenario: Validating the Sign Up button for the option "Sign up using mobile number" on  Register page.
   Given User is on Dietician website
    When User lands on Register page
    Then User should see a button with text "SIGN UP" in the Sign Up form

  Scenario: Validating the Sign up process with all fields being empty
    Given User is on Register page
    When User clicks SIGN UP Button in the Sign Up form with all fields empty .
    Then User should see a message "Mandatory fields cannot be empty"

  Scenario: Validating the Sign up process with invalid First Name
    Given User is on Register page
    When User clicks SIGN UP Button in the Sign Up form  by entering numeric text for Last Name, valid values for the remaining fields
    Then User should see a message "Invalid data entered for First Name"

  Scenario: Validating the Sign up process with invalid Last Name
    Given User is on Register page
    When User clicks SIGN UP Button in the Sign Up form  by entering numeric text for Last Name, valid values for the remaining fields
    Then User should see a message "Invalid data entered for Last Name"

  Scenario: Validating the Sign up process with invalid Mobile Number
    Given User is on Register page
    When User clicks SIGN UP Button in the Sign Up form  by entering Aphanumeric text for Mobile Number, valid values for the remaining fields .
    Then User should see a message "Invalid data entered for Mobile Number"

  Scenario:Validating the Sign up process with invalid Any other field
    Given User is on Register page
    When User clicks SIGN UP Button in the Sign Up form  by entering numeric text for Any other field, valid values for the remaining fields.
    Then User should see a message "Invalid data entered for Any other field"

  Scenario: Validating the Sign up process with invalid Password
    Given User is on Register page
    When User clicks SIGN UP Button in the Sign Up form  by entering invalid Password , valid values for the remaining fields.
    Then User should see a message "Invalid data entered for Password"

  Scenario Outline: Validating the Sign up process with all valid  input fields .
    Given User is on Register page
    When User clicks SIGN UP Button in the Sign Up form  by entering valid values for the all fields.
    Then User is re-directed to Sign In page.

     Examples:
      |firstName|lasttName|mobileNumber|otherField|emailAddress|password|
      |Shweta   |Tripathi|+1316565123|otherField|corporate.shweta@gmail.com|123Pass@123|

