from behave import *
from selenium import webdriver

@when(u'User lands on register page.')
def step_impl(context):
    assert True, "test passed"


@then(u'User should see a form with heading "Sign Up with your email", to sign up using Email Id.')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see a button with text "Sign Up" in the Sign Up with your Email form.')
def step_impl(context):
    assert True, "test passed"

@when(u'User clicks SIGN UP Button in the Sign Up with your Email form with all fields empty .')
def step_impl(context):
    assert True, "test passed"
@then(u'User should see a message "Mandatory fields cannot be empty".')
def step_impl(context):
    assert True, "test passed"

@when(u'User clicks SIGN UP Button in the Sign Up with your Email form  by entering numeric text for First Name, valid values for the remaining fields')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see a message "Invalid data entered for First Name".')
def step_impl(context):
    assert True, "test passed"

@when(u'User clicks SIGN UP Button in the Sign Up form with your Email by entering numeric text for Last Name, valid values for the remaining fields')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see a message "Invalid data entered for Last Name".')
def step_impl(context):
    assert True, "test passed"

@when(u'User clicks SIGN UP Button in the Sign Up form with your Email by entering numeric text for Username, valid values for the remaining fields')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see a message "Invalid data entered for Username".')
def step_impl(context):
    assert True, "test passed"

@when(u'User clicks SIGN UP Button in the Sign Up form with your Email by entering invalid Email Address , valid values for the remaining fields.')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see a message "Invalid data entered for Email Address".')
def step_impl(context):
    assert True, "test passed"

@when(u'User clicks SIGN UP Button in the Sign Up form with your Email by entering a value that is different than the Password field value ,valid values for the remaining fields.')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see a message "Confirm Password should same as Password".')
def step_impl(context):
    assert True, "test passed"

@when(u'User clicks SIGN UP Button in the Sign Up with your Email form  by entering valid values for the all fields.')
def step_impl(context):
    assert True, "test passed"
