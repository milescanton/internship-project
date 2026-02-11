from pages.add_project_page import AddProjectPage
from pages.base_page import Page
from pages.index_page import IndexPage
from pages.settings_page import SettingsPage
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):

        self.add_project_page = AddProjectPage(driver)
        self.base_page = Page(driver)
        self.index_page = IndexPage(driver)
        self.settings_page = SettingsPage(driver)
        self.sign_in_page = SignInPage(driver)

