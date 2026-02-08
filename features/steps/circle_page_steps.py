from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


BENEFIT_CELLS = (By.CSS_SELECTOR, "[class*='storycard--text']")


#this grabs the 3 main benefit cells, plus 2 other items on the page. Wasn't sure how else to grab only the 3 using find_elements
@then('Verify {expected_amount} benefit cells are shown')
def verify_benefit_cells(context, expected_amount):
    expected_amount = int(expected_amount)
    cells = context.driver.find_elements(*BENEFIT_CELLS)
    print(cells)
    assert len(cells) == expected_amount, f'Expected {expected_amount} benefit cells, but got {len(cells)}'
