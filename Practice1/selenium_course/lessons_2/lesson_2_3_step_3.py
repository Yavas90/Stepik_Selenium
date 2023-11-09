import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    alert = browser.switch_to.alert
    alert.accept()

    x_elem = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_elem.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    # Нажатие на кнопку submite
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    time.sleep(3)
    browser.quit()