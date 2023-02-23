import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    title = (By.XPATH, '//h1')

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        # print(f'\nОткрыт сайт: {self.get_current_url()}')
        self.compare_title('Интернет-магазин')

    # Этот метод ожидает, пока элемент, соответствующий указанному локатору, не станет видимым на странице
    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # Этот метод ожидает, пока элементы, соответствующий указанному локатору, не станут видимыми на странице
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    # Этот метод ожидает, пока элемент, соответствующий указанному локатору, не будет найден на странице.
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

        # Этот метод ожидает, пока элементы, соответствующие указанному локатору, не будут найдены на странице.
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    # Этот метод ожидает, пока элемент, соответствующий указанному локатору, не будет кликабельным.
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    # Этот метод получает текующий адрес
    def get_current_url(self):
        return self.driver.current_url

    # Этот метод скролит страницу
    def scroll_page(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def compare_title(self, title):
        title_value = self.element_is_visible(self.title).text
        assert title_value == title
        print(f'\nСтраница {self.get_current_url()} имеет заголовок \"{title_value}\"')

    def take_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        print('Скришот страницы')
        self.driver.save_screenshot(f'C:\\Users\\37533\AquaProjects\\auto_project\\screens\\screenshot_{now_date}.png')

