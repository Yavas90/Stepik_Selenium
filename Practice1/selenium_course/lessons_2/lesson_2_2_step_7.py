
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input[name=firstname]")
    input1.send_keys("Borov")

    input2 = browser.find_element(By.CSS_SELECTOR, "input[name=lastname]")
    input2.send_keys("Borovskyi")

    input3 = browser.find_element(By.CSS_SELECTOR, "input[name=email]")
    input3.send_keys("Borov@mail")

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(cur_dir, "NewFile.txt")
#Загрузка файла
    input_file = browser.find_element(By.CSS_SELECTOR, "#file")
    input_file.send_keys(file_path)


    # Нажатие на кнопку submite
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    time.sleep(3)
    browser.quit()