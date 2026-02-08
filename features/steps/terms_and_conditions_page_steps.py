from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    expected_text = 'Terms & Conditions'
    context.app.terms_and_conditions_page.verify_terms_and_conditions_page(expected_text)