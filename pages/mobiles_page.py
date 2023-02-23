import random
import time

from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger

class Mobile_page(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver

    # Locators

    release_filter = (By.XPATH, '(//div[@class="products-filters__section "])[1]')
    years = (By.XPATH, '(//div[@class="products-filters__checkboxes"])[1]/label/span/span[@class="js-filter-value"]')
    brand_filter = (By.XPATH, '//div[@class="products-filters__section__title" and contains(text(), "Бренд")]')
    brands = (By.XPATH, '(//div[@class="products-filters__section__body__inner"])[2]/label/span/span[@class="js-filter-value"]')
    phones = (By.XPATH, '//div[@class="products-list__body"]/div[@class="products__unit"]')

    # Actions

    def click_release_filter(self):
        print('Нажать на фильтр "Год выпуска"')
        self.element_is_clickable(self.release_filter).click()

    def click_brand_filter(self):
        print('Нажать на фильтр "Бренд"')
        self.element_is_clickable(self.brand_filter).click()



    # Methods

    def set_filters(self, release, brand):
        Logger.add_start_step(method='set_filters')
        self.click_release_filter()
        for year in self.elements_are_visible(self.years):
            if year.text == release:
                year.click()
                print(f'Выбрать год выпуска {year.text}')
                break

        time.sleep(5)

        self.click_brand_filter()
        for br in self.elements_are_visible(self.brands):
            if br.text == brand:
                br.click()
                print(f'Выбрать бренд {br.text}')
                break
        Logger.add_end_step(url=self.driver.current_url, method='set_filters')

    def random_phone(self):
        Logger.add_start_step(method='random_phone')
        # self.scroll_page()
        number = random.randrange(len(self.elements_are_present(self.phones)))
        print(f'Генерация случайного числа: {number}')
        n = 0
        for phone in self.elements_are_present(self.phones):
            n = n + 1
            if n == number:
                phone.click()
                print('Выбрать телефон')
                break
        Logger.add_end_step(url=self.driver.current_url, method='random_phone')


