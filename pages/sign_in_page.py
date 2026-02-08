from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):

    SIGN_IN_PAGE_TEXT = (By.XPATH, "//h1[contains(@class,'styles_ndsHeading__phw6r')]")
    TERMS_CONDITIONS_LINK = (By.XPATH, "//a[contains(@aria-label,'terms & conditions')]")

    def open_sign_in_page(self):
        self.open_url('/account')

    def verify_sign_in_page(self, expected_text):
        self.verify_text(expected_text, *self.SIGN_IN_PAGE_TEXT)

    def click_on_target_terms_conditions_link(self):
        self.wait_until_clickable_click(*self.TERMS_CONDITIONS_LINK)