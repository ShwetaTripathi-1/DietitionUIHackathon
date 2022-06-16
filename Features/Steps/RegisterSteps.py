from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

#test comment

@given('User is on Dietician website')
def User_is_on_Dietician_website(context):
    context.driver = webdriver.Chrome(
        executable_path="C:\\Users\\HP\\PycharmProjects\\DieticianUIHackathon\\Drivers\\chromedriver.exe")
    #context.driver.get("https://dsportalapp.herokuapp.com/home ")
    # context.webdriver = context.webdriver.Chrome(ChromeDriverManager().install())
    #context.webdriver = context.webdriver.Chrome(service=Service(ChromeDriverManager
                                                                 #(chrome_type=ChromeType.BRAVE).install()))
    context.driver.get("Url of the Dietician Website")


@when('User clicks Register link')
def User_clicks_Register_link(context):
    context.driver.find_element_by_xpath("Register link").click()


@then('user lands on Sign up page')
def user_lands_on_Signup_page(context):
    signup_text = context.driver.find_element_by_xpath("Sign up page heading").text()
    assert signup_text == " Sign UP "
    context.driver.close()


@when('User lands on Register page')
def User_lands_on_Register_page(context):
    context.driver.find_element_by_xpath("Register link").click()


@then('User should see a form with heading "Sign Up form", to sign up using mobile number')
def sign_up_heading_in_signup_with_mobile_form(context):
    signup_text = context.driver.find_element_by_xpath("Sign up page heading").text()
    assert signup_text == " Sign UP "
    context.driver.close()


@then('User should see a button with text "SIGN UP" in the Sign Up form')
def sign_up_btn_on_signup_with_mobile_form(context):
    btn_txt = context.driver.find_element_by_xpath("SignUp Button").text()
    assert btn_txt == "SIGN UP"
    context.driver.close()


@given('User is on Register page')
def User_is_on_Register_page(context):
    context.driver.find_element_by_xpath("Register link").click()


@when(
    'Enter Firstname "{f_name}", Lastname "{l_name}",Mobile number"{mobile_no}",Any other field"{other_field}",Email Address"{email_address}",Password"{pwd}"')
def enter_input_fields_with_multiple_data_in_signup_with_mobile(context, f_name, l_name, mobile_no, other_field,
                                                                email_address, pwd):
    context.driver.find_element_by_xpath(" First name").send_keys(f_name)
    context.driver.find_element_by_xpath(" Lastname").send_keys(l_name)
    context.driver.find_element_by_xpath(" Mobile number").send_keys(mobile_no)
    context.driver.find_element_by_xpath(" Any other field").send_keys(other_field)
    context.driver.find_element_by_xpath("Email Address").send_keys(email_address)
    context.driver.find_element_by_xpath(" Password").send_keys(pwd)


@when('User clicks SIGN UP Button in the Sign Up form')
def signup_button_in_signup_form(context):
    context.driver.find_element_by_xpath("Sign Up Button").click()


@then('user successfully Sign Up')
def user_successfully_Sign_Up(context):
    try:
        home_txt = context.driver.find_element_by_xpath("home page heading").text()
    except:
        context.driver.close()
        assert False, "Test Failed"
    if home_txt == "Lorem ipsum dolor":
        context.driver.close()
    assert True, "test passed"


@when('User lands on register page.')
def User_lands_on_register_page(context):
    context.driver.find_element_by_xpath("Register link").click()


@then('User should see a form with heading "Sign Up with your email", to sign up using Email Id.')
def signup_heading_in_signup_with_your_email_form(context):
    signup_email_text = context.driver.find_element_by_xpath("Sign up with your email").text()
    assert signup_email_text == " Sign up with your email "
    context.driver.close()


@then('User should see a button with text "Sign Up" in the Sign Up with your Email form.')
def signup_button_in_signup_with_your_email_form(context):
    email_btn_txt = context.driver.find_element_by_xpath("SignUp Button").text()
    assert email_btn_txt == "SIGN UP"
    context.driver.close()


@when(
    'Enter Firstname "{name_email}", Lastname "{lname_email}",User Name"{username_email}",Email Address"{email_add}",Password"{email_password}",Confirm Password"{confirm_pwd}"')
def enter_input_fields_with_multiple_data(context, name_email, lname_email, username_email, email_add, email_password,
                                          confirm_pwd):
    context.driver.find_element_by_xpath("Firstname").send_keys(name_email)
    context.driver.find_element_by_xpath("Lastname").send_keys(lname_email)
    context.driver.find_element_by_xpath("User Name").send_keys(username_email)
    context.driver.find_element_by_xpath("Email Address").send_keys(email_add)
    context.driver.find_element_by_xpath("Password").send_keys(email_password)
    context.driver.find_element_by_xpath("Confirm Password").send_keys(confirm_pwd)


@when('User clicks SIGN UP Button in the Sign Up with your email')
def User_clicks_SIGN_UP_Button_in_the_Sign_Up_with_your_email(context):
    context.driver.find_element_by_xpath("Sign Up Button")


@when('User clicks Facebook Button in the Sign Up with your Email form .')
def signup_facebook_link(context):
    context.driver.find_element_by_xpath("facebook link").click()


@then('User successfully login with Facebook account.')
def facebook_signup(context):
    facebook_account_page = context.driver.find_element_by_xpath("Facebook account page heading").text()
    assert facebook_account_page == "Facebook account page heading"
    context.driver.close()


@when('User clicks Google Button in the Sign Up with your Email form .')
def signup_google_link(context):
    context.driver.find_element_by_xpath("google button link")


@then('User successfully login with Google account.')
def google_signup(context):
    google_account_page = context.driver.find_element_by_xpath("google account page heading").text()
    assert google_account_page == "google account page heading"
    context.driver.close()


@when('User clicks "Log in here" link.')
def Log_in_here_link(context):
    context.driver.find_element_by_xpath("log in here link").click()


@then(u'User is re-directed to Sign In Page')
def User_is_redirected_to_Sign_In_Page(context):
    sign_in_page_text = context.driver.find_element_by_xpath("sign in page heading").text()
    assert sign_in_page_text == "Sign In"
    context.driver.close()
