import time

from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver


    #Locators

    mobiles_category = (By.XPATH, '//a[@class="popular__category"][@href="https://shop.mts.by/phones/"]')
    title = (By.XPATH, '//h1')

    #Actions

    def click_mobile_category_link(self):
        print('Нажать на категорию "Смартфоны"')
        self.element_is_present(self.mobiles_category).click()


    #Methods

    def open_category_mobiles(self):
        Logger.add_start_step(method='open_category_mobiles')
        self.scroll_page()
        print("Прокрутить страницу")
        self.click_mobile_category_link()
        self.compare_title('Смартфоны')
        Logger.add_end_step(url=self.driver.current_url, method='open_category_mobiles')