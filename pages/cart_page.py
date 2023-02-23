import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger

class Cart_page(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver

    # Locators

    fullname_field = (By.XPATH, '//input[@name="properties[NAME]"]')
    phone_number_field = (By.XPATH, '//input[@name="properties[PERSONAL_PHONE]"]')
    email_field = (By.XPATH, '//input[@name="properties[EMAIL]"]')
    address_field = (By.XPATH, '//input[@name="properties[PERSONAL_STREET]"]')
    home_field = (By.XPATH, '//input[@name="properties[HOME]"]')
    apartment_field = (By.XPATH, '//input[@name="properties[FLAT]"]')
    order_button = (By.XPATH, '//a[contains(text(),"Оформить заказ")]')



    # Actions

    def input_fullname_field(self, value):
        print(f'Написать {value} в поле "ФИО"')
        self.element_is_visible(self.fullname_field).send_keys(value)

    def input_phone_number_field(self, value):
        print(f'Написать {value} в поле "Контактный телефон"')
        self.element_is_visible(self.phone_number_field).send_keys(value)

    def input_address_field(self, value):
        print(f'Написать {value} в поле "Улица"')
        self.element_is_visible(self.address_field).send_keys(value)

    def input_email_field(self, value):
        print(f'Написать {value} в поле "Электронная почта"')
        self.element_is_visible(self.email_field).send_keys(value)

    def input_home_field(self, value):
        print(f'Написать {value} в поле "Дом"')
        self.element_is_visible(self.home_field).send_keys(value)

    def input_apartment_field(self, value):
        print(f'Написать {value} в поле "Квартира"')
        self.element_is_visible(self.apartment_field).send_keys(value)

    def click_order_button(self):
        print('Нажать на кнопку "Оформить заказ"')
        self.element_is_clickable(self.order_button).click()


    # Methods

    def set_contacts(self, fullname, number, email, street, building, apartment):
        Logger.add_start_step(method='set_contacts')
        self.scroll_page()
        self.input_fullname_field(fullname)
        self.input_phone_number_field(number)
        self.input_email_field(email)
        self.input_address_field(street)
        self.input_home_field(building)
        self.input_apartment_field(apartment)
        self.click_order_button()
        self.take_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='set_contacts')



