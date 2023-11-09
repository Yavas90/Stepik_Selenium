import math
from selenium.common.exceptions import NoAlertPresentException
from .Base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        basket_btn.click()

    def should_be_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Basket button is not presented"

    def should_be_product_page(self):
        assert "?promo=offer" in self.browser.current_url, "Подстрока ?promo=offer нет в URL"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_SUM), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_SUM).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price == message_basket_total, "No product price in the message"

    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITTLE), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_TITTLE).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert product_name == message, "No product name in the message"
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Message about adding is presented"

    def should_be_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Message about adding is not disappeared"