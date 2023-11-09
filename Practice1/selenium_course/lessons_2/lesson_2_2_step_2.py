import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def sum(x1, x2):
    return str(int(x1) + int(x2))

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elem1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    x1 = elem1.text
    #x1 = int(x1)

    elem2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    x2 = elem2.text
    #x2 = int(x2)
    #e_sum = x1 + x2
    e_sum = sum(x1, x2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(e_sum))

#Нажатие на кнопку submite
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    time.sleep(5)
    browser.quit()