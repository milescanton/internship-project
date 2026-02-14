from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SettingsPage(Page):

    ADD_A_PROJECT =  (By.CSS_SELECTOR, "a[href='/add-a-project']")

    def click_on_add_a_project(self):
        sleep(3)
        self.click(*self.ADD_A_PROJECT)