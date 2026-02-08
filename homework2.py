from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()




#Practice with locators

#Amazon Logo
#driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Email Field
#driver.find_element(By.ID, "ap_email")

#Continue Button
#driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

#Condition of Use Link
#driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

#Privacy of Notice Link
#driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

#Need Help Link
#driver.find_element(By.ID, "ap-other-signin-issues-link")

#Forgot your Password Link
#driver.find_element(By.ID, "auth-fpp-link-bottom")

#Create your Amazon Account Button
#driver.find_element(By.ID, "createAccountSubmit")



#Sign-In Page Test Case

# open the url
driver.get('https://www.target.com/')

#Click Account Button
driver.find_element(By.ID, 'account-sign-in').click()

#Click Sign-In Button
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

#Wait for page to load
sleep(3)

#Verify "Sign in or create account" text
expected_text = 'Sign in or create account'
actual_text = driver.find_element(By.XPATH, "//h1[contains(@class,'styles_ndsHeading__phw6r')]").text
assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
print(actual_text)

#Verify 'Sign in with passkey' button
button_text = driver.find_element(By.XPATH, "//button[text()='Sign in with passkey']").text
print(button_text)