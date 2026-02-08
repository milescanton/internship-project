from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Sign In page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()

@when('Click on Target Terms and Conditions link')
def click_on_target_terms_conditions_link(context):
    context.app.sign_in_page.click_on_target_terms_conditions_link()

@then('Verify Sign In page')
def verify_sign_in_page(context):
    expected_text = 'Sign in or create account'
    context.app.sign_in_page.verify_sign_in_page(expected_text)
