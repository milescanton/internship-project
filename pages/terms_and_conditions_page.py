from selenium.webdriver.common.by import By
from pages.base_page import Page


class TermsAndConditionsPage(Page):

    TERMS_AND_CONDITIONS_PAGE_TEXT = (By.CSS_SELECTOR, "[data-test='page-title']")

    def verify_terms_and_conditions_page(self, expected_text):
        self.verify_text(expected_text, *self.TERMS_AND_CONDITIONS_PAGE_TEXT)