Feature: Dietician Website Register Page
  Scenario: Validating the title of Register Page
    Given User is on Dietician website
    When User lands on Register page
    Then User should see the title of the page as "Register"


  Scenario: Validating the Register page mandatory fields
   Given User is on Dietician website
    When User lands on Register page
    Then User should see all mandatory flields with star symbol on top of those fields


  Scenario: Validating the Sign Up form heading
    Given User is on Dietician website
    When User lands on Register page
    Then User should see a form with heading "Sign Up form", to sign up using mobile number



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
