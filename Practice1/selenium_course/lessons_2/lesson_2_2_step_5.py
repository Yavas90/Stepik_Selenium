import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_elem.text
    y = calc(x)

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    #Прокрутка к нужному элементу
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    time.sleep(2)

    # Нажатие на кнопку submite
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    time.sleep(3)
    browser.quit()