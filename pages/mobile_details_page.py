import time

from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger

class Mobile_details_page(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver


    # Locators

    payment_field = (By.XPATH, '(//div[@class="select__header"])[1]')
    payment_type = (By.XPATH, '//div[@data-value="fullInstallment" and contains(text(), "Единый платеж")]')
    add_cart_button = (By.XPATH, '(//a[@id="addToBasket"])[4]')
    go_cart_button = (By.CSS_SELECTOR, '.item__price__controls--in-cart span:nth-child(2)')

    # Actions

    def click_payment_field(self):
        print('Нажать на поле "Платежи"')
        self.element_is_clickable(self.payment_field).click()

    def click_payment_type(self):
        print('Нажать на тип платежа')
        self.element_is_visible(self.payment_type).click()

    def click_add_cart_button(self):
        print('Нажать на кнопку "Добавить в корзину"')
        self.element_is_clickable(self.add_cart_button).click()

    def click_go_cart_button(self):
        print('Нажать на кнопку "Перейти в корзину"')
        self.element_is_present(self.go_cart_button).click()


    # Methods

    def go_cart(self):
        Logger.add_start_step(method='go_cart')
        self.click_payment_field()
        self.click_payment_type()
        self.click_add_cart_button()
        time.sleep(5)
        self.click_go_cart_button()

        self.compare_title('Корзина')
        Logger.add_end_step(url=self.driver.current_url, method='go_cart')




