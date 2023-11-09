import pytest
import time

from .Pages.basket_page import BasketPage
from .Pages.login_page import LoginPage
from .Pages.product_page import ProductPage

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/")
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
@pytest.mark.need_review
@pytest.mark.parametrize('end_link',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, end_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{end_link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_be_basket_btn()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_guest_cant_see_success_message_after_adding_product_to_basket()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_guest_cant_see_success_message_after_adding_product_to_basket()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/")
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_text_in_basket()
    basket_page.should_not_be_product_in_basket()

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = LoginPage.generate_password(self, 10)
        page.register_new_user(email, password)
        page.user_login_to_account()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_guest_cant_see_success_message_after_adding_product_to_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()
