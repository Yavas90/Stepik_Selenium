from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    ENTER_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    ENTER_PASS_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    ENTER_BTN = (By.CSS_SELECTOR, "#login_form > button")
    REG_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.CSS_SELECTOR, "#register_form > button")

    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.ID, "id_registration-email")
    PASS = (By.ID, "id_registration-password1")
    CONF_PASS = (By.ID, "id_registration-password2")
    BTN_REG = (By.NAME, "registration_submit")
    LOGOUT = (By.ID, "logout_link")

class ProductPageLocators():
#Кнопка добавить в корзину
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
#Alert о добавлении товара в корзину
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner > strong")
#Название товара
    PRODUCT_TITTLE = (By.CSS_SELECTOR, "div.product_main h1")
#Сумма в корзине
    MESSAGE_BASKET_SUM = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
#Цена товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
#Кнопка добавить в корзину
    BASKET_BTN = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketLocators():
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner a")
    BASKET_EMPTY_PRODUCT = (By.CSS_SELECTOR, ".carousel")