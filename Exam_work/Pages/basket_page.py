from .Base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_EMPTY_PRODUCT), "В корзине находится товар, " \
                                                                                          "хотя не должен! "

    def should_be_empty_text_in_basket(self):
        empty_text = self.browser.find_element(*BasketLocators.BASKET_EMPTY_TEXT)
        assert empty_text.text in "Continue shopping", "В корзине находится товар, хотя не должен быть!"