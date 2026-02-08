from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):

    EMPTY_CART_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    empty_cart_msg = 'Your cart is empty'
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def open_cart_page(self):
        self.open_url('/cart')

    def verify_empty_cart_msg(self):
        self.verify_partial_text(self.empty_cart_msg, *self.EMPTY_CART_MSG)

    def verify_product(self, expected_product):
        product_in_cart = self.find_element(*self.PRODUCT_NAME).text
        self.verify_partial_text(expected_product, *self.PRODUCT_NAME)
        print(f'The expected product name: {expected_product} matches the actual product name: {product_in_cart}')





