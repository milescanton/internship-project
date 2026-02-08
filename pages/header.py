from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class Header(Page):

    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    ACCOUNT_BTN = (By.ID, 'account-sign-in')
    SIGN_IN_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(10)

    def click_cart_icon(self):
        self.wait_until_clickable_click(*self.CART_ICON)

    def click_account_btn(self):
        self.wait_until_clickable_click(*self.ACCOUNT_BTN)

    def click_sign_in_btn(self):
        self.wait_until_clickable_click(*self.SIGN_IN_BTN)