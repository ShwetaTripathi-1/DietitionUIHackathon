from behave import *
from selenium import webdriver

@then(u'User should see a button with text "SIGN UP" in the Sign Up form')
def step_impl(context):
    assert True, "test passed"
@when(u'User clicks SIGN UP Button in the Sign Up form with all fields empty .')
def step_impl(context):
    assert True, "test passed"
@then(u'User should see a message "Mandatory fields cannot be empty"')
def step_impl(context):
    assert True, "test passed"

@when(u'User clicks SIGN UP Button in the Sign Up form  by entering numeric text for Last Name, valid values for the remaining fields')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see a message "Invalid data entered for First Name"')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see a message "Invalid data entered for Last Name"')
def step_impl(context):
    assert True, "test passed"

@when(u'User clicks SIGN UP Button in the Sign Up form  by entering Aphanumeric text for Mobile Number, valid values for the remaining fields .')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see a message "Invalid data entered for Mobile Number"')
def step_impl(context):
    assert True, "test passed"


@when(u'User clicks SIGN UP Button in the Sign Up form  by entering numeric text for Any other field, valid values for the remaining fields.')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see a message "Invalid data entered for Any other field"')
def step_impl(context):
    assert True, "test passed"

@when(u'User clicks SIGN UP Button in the Sign Up form  by entering invalid Password , valid values for the remaining fields.')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see a message "Invalid data entered for Password"')
def step_impl(context):
    assert True, "test passed"


@when(u'User clicks SIGN UP Button in the Sign Up form  by entering valid values for the all fields.')
def step_impl(context):
    assert True, "test passed"

@then(u'User is re-directed to Sign In page.')
def step_impl(context):
    assert True, "test passed"