from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddProjectPage(Page):

    NAME_INPUT = (By.CSS_SELECTOR, "[name='Your-name']")
    COMPANY_INPUT = (By.CSS_SELECTOR, "[name='Your-company-name']")
    ROLE_INPUT = (By.CSS_SELECTOR, "[name='Role']")
    AGE_INPUT = (By.CSS_SELECTOR, "[name='Age-of-the-company']")
    COUNTRY_INPUT = (By.CSS_SELECTOR, "[name='Country']")
    PROJECT_NAME_INPUT = (By.CSS_SELECTOR, "[name='Name-project']")
    PHONE_INPUT = (By.CSS_SELECTOR, "[name='Phone']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='Email-add-project']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Send an application')]")

    FIELD_MAP = {
        "name": NAME_INPUT,
        "company": COMPANY_INPUT,
        "role": ROLE_INPUT,
        "age": AGE_INPUT,
        "country": COUNTRY_INPUT,
        "project_name": PROJECT_NAME_INPUT,
        "phone": PHONE_INPUT,
        "email": EMAIL_INPUT
    }

    def add_info(self, data: dict):
        for field, value in data.items():
            locator = self.FIELD_MAP.get(field)
            if locator:
                element = self.driver.find_element(*locator)
                element.clear()
                element.send_keys(value)
            else:
                raise ValueError(f"No locator found for field: {field}")


    def verify_info(self, expected_data: dict):
        for field, expected_value in expected_data.items():
            locator = self.FIELD_MAP.get(field)
            if locator:
                element = self.driver.find_element(*locator)
                actual_value = element.get_attribute("value")

                assert actual_value == expected_value, (
                    f"Field '{field}' mismatch. "
                    f"Expected: {expected_value}, "
                    f"Actual: {actual_value}"
                )
            else:
                raise ValueError(f"No locator found for field: {field}")


    def verify_submit_button(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.SUBMIT_BUTTON)
            )
            return True
        except:
            return False

