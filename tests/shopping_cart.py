# -*- coding: UTF-8 -*-
"""
Test shopping cart
Version 1.1
Author Joanna Dmochowska
"""

from locators import SearchFormLocators
from tests.base_test import BaseTest
from time import sleep


class ShoppingCart(BaseTest):
    """Testing the product in the cart"""

    def test_check_price_product(self):
        """Price product should be equal cart sum"""
        self.driver.find_element(*SearchFormLocators.SEARCH_BTN).click()
        self.driver.find_element(*SearchFormLocators.SEARCH_FIELD).send_keys("biale buty")
        sleep(3)
        self.driver.find_element(*SearchFormLocators.SHOES).click()
        el_price = self.driver.find_element(*SearchFormLocators.PRICE_SHOES)
        price = el_price.text
        print(price)
        price = price.split()
        print(price)
        price = price[0]
        price = price.replace(",", ".")
        print(price)

        self.driver.find_element(*SearchFormLocators.SIZE_SHOES).click()
        self.driver.find_element(*SearchFormLocators.ADD_BASKET).click()
        self.driver.find_element(*SearchFormLocators.ORDER).click()
        self.driver.find_element(*SearchFormLocators.PLUS_BTN).click()

        price_b = self.driver.find_element(*SearchFormLocators.PRICE_BASKET)
        sleep(5)
        price_basket = price_b.text
        print(price_basket)
        price_basket = price_basket.split()
        print(price_basket)
        price_basket = price_basket[0]
        print(price_basket)
        price_basket = price_basket.replace(",", ".")
        print(price_basket)

        self.assertEqual(2 * float(price), float(price_basket))
