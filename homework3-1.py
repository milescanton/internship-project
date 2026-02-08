#Homework 3 Part 1

#Create your account
driver.findelement(By.CSS_Selector, "[class*='fs-headline1'][class*='fw-bold']")

#Terms of service
driver.findelement(By.CSS_Selector, ".js-terms")

#Email field
driver.find_element(By.CSS_Selector, '#email')

#Password field
driver.find_element(By.CSS_Selector, '#password')

#Submit button
driver.find_element(By.CSS_Selector, '#submit-button')

#Google sign-up button
driver.findelement(By.CSS_Selector, "[class*='s-btn__icon'][class*='s-btn__google']")

#GitHun sign-up button
driver.find_element(By.CSS_Selector, "[class*='s-btn__icon'][class*='s-btn__github']")