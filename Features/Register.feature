Feature: Dietician Website Register Page

  Scenario: Validating the title of Register Page
    Given User is on Dietician website
    When User clicks Register link
    Then  user lands on Sign up page


  Scenario: Validating the Sign Up form heading
    Given User is on Dietician website
    When User lands on Register page
    Then User should see a form with heading "Sign Up form", to sign up using mobile number

  Scenario: Validating the Sign Up button for the option "Sign up using mobile number" on  Register page.
    Given User is on Dietician website
    When User lands on Register page
    Then User should see a button with text "SIGN UP" in the Sign Up form

  Scenario Outline: Validating the Sign up process with multiple  input fields .
    Given User is on Register page

    When Enter Firstname "<firstName>", Lastname "<lastName>",Mobile number"<mobileNumber>",Any other field"<Any otherField>",Email Address"<emailAddress>",Password"<password>"
    And User clicks SIGN UP Button in the Sign Up form
    Then user successfully Sign Up

    Examples:
      | firstName    | lastName     | mobileNumber | Any otherField | emailAddress | password     |
      | Empty field  | Empty field  | Empty field  | Empty field    | Empty field  | Empty field  |
      | Invalid data | Valid data   | Valid data   | Valid data     | Valid data   | Valid data   |
      | Valid data   | Invalid data | Valid data   | Valid data     | Valid data   | Valid data   |
      | Valid data   | Valid data   | Invalid data | Valid data     | Valid data   | Valid data   |
      | Valid data   | Valid data   | Valid data   | Invalid data   | Valid data   | Valid data   |
      | Valid data   | Valid data   | Valid data   | Valid data     | invalid data | Valid data   |
      | Valid data   | Valid data   | Valid data   | Valid data     | Valid data   | Invalid data |
      | Valid data   | Valid data   | Valid data   | Valid data     | Valid data   | Valid data   |


  Scenario: Validating the Sign Up form heading
    Given User is on Dietician website
    When User lands on register page.
    Then User should see a form with heading "Sign Up with your email", to sign up using Email Id.

  Scenario: Validating the Sign Up button for the option "Sign up using Email Id" on  Register page.
    Given User is on Dietician website
    When User lands on register page.
    Then User should see a button with text "Sign Up" in the Sign Up with your Email form.

  Scenario Outline: Validating the Sign up process with multiple parameters
    Given User is on Register page
    When User clicks SIGN UP Button in the Sign Up with your email
    And Enter Firstname "<firstName>", Lastname "<lastName>",User Name"<userName>",Email Address"<emailAddress>",Password"<password>",Confirm Password"<confirmPassword>"
    Then user successfully Sign Up
    Examples:
      | firstName    | lastName     | userName     | emailAddress | password     | confirmPassword |
      | Empty field  | Empty field  | Empty field  | Empty field  | Empty field  | Empty field     |
      | Invalid data | Valid data   | Valid data   | Valid data   | Valid data   | Valid data      |
      | Valid data   | Invalid data | Valid data   | Valid data   | Valid data   | Valid data      |
      | Valid data   | Valid data   | Invalid data | Valid data   | Valid data   | Valid data      |
      | Valid data   | Valid data   | Valid data   | Invalid data | Valid data   | Valid data      |
      | Valid data   | Valid data   | Valid data   | Valid data   | invalid data | Valid data      |
      | Valid data   | Valid data   | Valid data   | Valid data   | Valid data   | Invalid data    |
      | Valid data   | Valid data   | Valid data   | Valid data   | Valid data   | Valid data      |

  Scenario: Validating the Sign up process with Facebook
    Given User is on Register page
    When User clicks Facebook Button in the Sign Up with your Email form .
    Then User successfully login with Facebook account.

  Scenario: Validating the Sign up process with Google .
    Given User is on Register page
    When  User clicks Google Button in the Sign Up with your Email form .
    Then User successfully login with Google account.

  Scenario: Validating Log In Here link
    Given User is on Register page
    When User clicks "Log in here" link.
    Then User is re-directed to Sign In Page

