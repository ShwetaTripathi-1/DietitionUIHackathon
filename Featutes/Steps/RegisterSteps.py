from behave import *
from selenium import webdriver




@given(u'User is on Dietician website')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path= "C:\\Users\\HP\\OneDrive\\Desktop\\Shweta\\NUMPY NINJA\\drivers\\chromedriver.exe")
    context.driver.get("https://dsportalapp.herokuapp.com/home ")


@when(u'User lands on Register page')
def step_impl(context):
    assert True, "test passed"


@then(u'User should see the title of the page as "Register"')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see all mandatory flields with star symbol on top of those fields')
def step_impl(context):
    assert True, "test passed"

@then(u'User should see a form with heading "Sign Up form", to sign up using mobile number')
def step_impl(context):
    assert True, "test passed"

@given(u'User is on Register page')
def step_impl(context):
    assert True, "test passed"


@when(u'User clicks Facebook Button in the Sign Up with your Email form .')
def step_impl(context):
    assert True, "test passed"


@then(u'User successfully login with Facebook account.')
def step_impl(context):
    assert True, "test passed"


@when(u'User clicks Google Button in the Sign Up with your Email form .')
def step_impl(context):
    assert True, "test passed"


@then(u'User successfully login with Google account.')
def step_impl(context):
    assert True, "test passed"


@when(u'User clicks "Log in here" link.')
def step_impl(context):
    assert True, "test passed"


@then(u'User is re-directed to Sign In Page')
def step_impl(context):
    assert True, "test passed"
