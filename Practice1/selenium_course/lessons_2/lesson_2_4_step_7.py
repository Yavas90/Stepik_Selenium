import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

#ожидание пока цена не станет $100
    price100 = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btn1 = browser.find_element(By.CSS_SELECTOR, "#book")
    btn1.click()

    x_elem = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_elem.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    # Нажатие на кнопку submite
    button = browser.find_element(By.CSS_SELECTOR, "#solve.btn.btn-primary")
    button.click()

finally:
    time.sleep(3)
    browser.quit()