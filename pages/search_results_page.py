from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):

    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")  # always clicks on 1st Add to cart btn
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    SIDE_NAV_VIEW_CART_BTN = (By.CSS_SELECTOR, "[href='/cart']")

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TEXT)

    def click_add_to_cart_btn(self):
        self.click(*self.ADD_TO_CART_BTN)

    def store_product_name(self):
        return self.store_text(*self.SIDE_NAV_PRODUCT_NAME)

    def click_2nd_add_to_cart_btn(self):
        self.wait_until_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BTN)

    def click_view_cart_btn(self):
        self.wait_until_clickable_click(*self.SIDE_NAV_VIEW_CART_BTN)