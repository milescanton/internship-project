from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class IndexPage(Page):

    SETTINGS = (By.CSS_SELECTOR, "a[href='/settings']")

    def click_on_settings(self):
        sleep(3)
        self.click(*self.SETTINGS)

