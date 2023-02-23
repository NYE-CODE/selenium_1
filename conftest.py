import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions



@pytest.fixture(scope="session")
def driver():
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()