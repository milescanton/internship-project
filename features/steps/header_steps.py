from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


TARGET_CIRCLE = (By.CSS_SELECTOR, "[data-test='@web/GlobalHeader/UtilityHeader/TargetCircle']")


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()


@when('Click Account button')
def click_account_btn(context):
    context.app.header.click_account_btn()


@then('Click Sign In button')
def click_sign_in_btn(context):
    context.app.header.click_sign_in_btn()


# @when('Click Target Circle')
# def click_target_circle(context):
#     context.driver.find_element(*TARGET_CIRCLE).click()
