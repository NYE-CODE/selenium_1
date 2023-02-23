import time

import pytest

from base.base_class import Base
from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.mobile_details_page import Mobile_details_page
from pages.mobiles_page import Mobile_page


def test_buy_phone(driver):
    browser = Base(driver, 'https://shop.mts.by')
    browser.open()

    main = Main_page(driver, 'https://shop.mts.by')
    main.open_category_mobiles()

    mobile = Mobile_page(driver, 'https://shop.mts.by')
    mobile.set_filters('2020', 'Samsung')

    time.sleep(3)

    mobile.random_phone()

    details = Mobile_details_page(driver, 'https://shop.mts.by')
    details.go_cart()

    order = Cart_page(driver, 'https://shop.mts.by')
    order.set_contacts('Test Testovuy', '+3751234567890', 'test@test.by', 'Pushkina', '5/2', '1')


