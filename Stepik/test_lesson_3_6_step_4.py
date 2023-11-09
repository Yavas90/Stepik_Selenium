import math
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


# link = "https://stepik.org/lesson/236895/step/1"

@pytest.mark.parametrize("links",
                         ["https://stepik.org/lesson/236895/step/1",
                          "https://stepik.org/lesson/236896/step/1",
                          "https://stepik.org/lesson/236897/step/1",
                          "https://stepik.org/lesson/236898/step/1",
                          "https://stepik.org/lesson/236899/step/1",
                          "https://stepik.org/lesson/236903/step/1",
                          "https://stepik.org/lesson/236904/step/1",
                          "https://stepik.org/lesson/236905/step/1"])
class TestAuthorization:

    def test_auth(self, browser, links):
        browser.implicitly_wait(5)
        browser.get(links)

        # ожидание загрузки кнопки вход
        sing_in = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ember33")))
        sing_in.click()
        # поиск поля ввода email
        in_login = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
        in_login.send_keys("ia.vasilev@petrovich.tech")
        # поиск поля ввода пароля
        in_pass = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        in_pass.send_keys("Lamantina1990!")
        # нажатие кнопки отправить
        btn_enter = browser.find_element(By.CSS_SELECTOR, "#login_form > button")
        btn_enter.click()

        # ожидание загрузки поля для ввода
        in_answer = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")))
        answer = math.log(int(time.time()))
        in_answer.send_keys(answer)
        # ожидание загрузки кнопки отправить
        btn_sbm = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#ember78 > div > section > div > div.attempt__inner > div.attempt__actions > button")))
        btn_sbm.click()

        a_text = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".smart-hints__hint")))
        answer_text = a_text.text

        assert "Correct!" == answer_text, "Wrong result!"
        print(answer_text)
