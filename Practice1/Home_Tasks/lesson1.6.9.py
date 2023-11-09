from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input_name = browser.find_element(By.CSS_SELECTOR, "input.first:required").send_keys("abs")
    input_last_name = browser.find_element(By.CSS_SELECTOR,  "input.second:required").send_keys('asd')
    input_mail = browser.find_element(By.CSS_SELECTOR, 'input.third:required').send_keys('asd@asd.com')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    welcome_text_1 = browser.find_element(By.TAG_NAME, 'h1')

    assert "Congratulations! You have successfully registered!" == welcome_text_1.text

finally:

    time.sleep(5)
    browser.quit()

