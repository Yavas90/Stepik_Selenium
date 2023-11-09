import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class UniqueSelectors(unittest.TestCase):
    def test_unSel1(self):

            link1 = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link1)

            input1 = browser.find_element(By.CSS_SELECTOR, '.form-group:nth-child(1) > .form-control.first')
            input1.send_keys("Borov")

            input2 = browser.find_element(By.CSS_SELECTOR, '.form-group:nth-child(2) > .form-control.second')
            input2.send_keys("Borovskyi")

            input3 = browser.find_element(By.CSS_SELECTOR, '.form-group:nth-child(3) > .form-control.third')
            input3.send_keys("Borov@mail")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEquals("Congratulations! You have successfully registered!", welcome_text, "Test OK")

            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_unSel2(self):
            link2 = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link2)

            input1 = browser.find_element(By.CSS_SELECTOR, '.form-group:nth-child(1) > .form-control.first')
            input1.send_keys("Borov")

            input2 = browser.find_element(By.CSS_SELECTOR, '.form-group:nth-child(2) > .form-control.second')
            input2.send_keys("Borovskyi")

            input3 = browser.find_element(By.CSS_SELECTOR, '.form-group:nth-child(3) > .form-control.third')
            input3.send_keys("Borov@mail")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEquals("Congratulations! You have successfully registered!", welcome_text, "Test OK")

            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == "__main__":
    unittest.main()