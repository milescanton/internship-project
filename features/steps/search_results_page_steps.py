from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


# LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
# PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
# PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)


@then('Click Add to Cart Button')
def click_add_to_cart_btn(context):
    sleep(10)
    context.app.search_results_page.click_add_to_cart_btn()  # always clicks on 1st Add to cart btn


@then('Store product name')
def store_product_name(context):
    context.product_before_adding = context.app.search_results_page.store_product_name()
    print(context.product_before_adding)


@then('Click 2nd Add to Cart Button')
def click_2nd_add_to_cart_btn(context):
    context.app.search_results_page.click_2nd_add_to_cart_btn()


@then('Click View Cart Button')
def click_view_cart_btn(context):
    context.app.search_results_page.click_view_cart_btn()


# @then('Verify that every product has a name and an image')
# def verify_products_name_img(context):
#     # To see ALL listings (comment out if you only check top ones):
#     # context.driver.execute_script("window.scrollBy(0,2000)", "")
#     # sleep(0.5)
#     # context.driver.execute_script("window.scrollBy(0,2000)", "")
#     # sleep(0.5)
#     # If you ever need to scroll up, use negative numbers: context.driver.execute_script("window.scrollBy(0, -2000)", "")
#
#     products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]
#     for product in products[:8]:
#         title = product.find_element(*PRODUCT_TITLE).text
#         assert title, 'Product title not shown'
#         print(f'🟢{title}')
#         product.find_element(*PRODUCT_IMG)

