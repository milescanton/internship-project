from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then('Empty Cart message is shown')
def verify_empty_cart_msg(context):
    context.app.cart_page.verify_empty_cart_msg()


@then('Verify Cart')
def verify_product(context):
    context.app.cart_page.verify_product(context.product_before_adding)

