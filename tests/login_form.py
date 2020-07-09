# -*- condig: UTF-8 -*-
"""
Test login functionality
Version 1.1
Author Joanna Dmochowska
"""

from tests.base_test import BaseTest
from locators import LoginPageLocators
import unittest
from library import GetData
from ddt import ddt, data, unpack
import os

# Get actual DIR
CUR_DIR = os.path.dirname(os.path.abspath(__file__))

@ddt
class LoginForm(BaseTest):
    """Testing the login form."""

    def test_empty_login_form(self):
        """Register with empty data should fail."""

        self.driver.find_element(*LoginPageLocators.LOG_IN_BTN).click()
        self.driver.find_element(*LoginPageLocators.FILL_EMAIL).send_keys("")
        self.driver.find_element(*LoginPageLocators.FILL_PASS).send_keys("")
        self.driver.find_element(*LoginPageLocators.SIGN_IN_BTN).submit()
        self.driver.find_element(LoginPageLocators.ERROR_EL_LOGIN)
        error_elements = self.driver.find_elements(*LoginPageLocators.ERROR_EL_LOGIN)

        for el in error_elements:
            if(el.text == "To pole jest obowiązkowe."):
                error_is_visible = True
                break
            else:
                error_is_visible = False

        self.assertTrue(error_is_visible)

    file_path = os.path.join(CUR_DIR, '..', 'data/incorrect_emails_account.csv')

    @data(*GetData.get_data(file_path))
    @unpack
    def test_incorrect_email(self, email):
        """Register with incorrect email should fail."""

        self.driver.find_element(*LoginPageLocators.LOG_IN_BTN).click()
        self.driver.find_element(*LoginPageLocators.FILL_EMAIL).send_keys(email)
        self.driver.find_element(*LoginPageLocators.FILL_PASS).send_keys("Test")
        self.driver.find_element(*LoginPageLocators.SIGN_IN_BTN).submit()
        error_elements = self.driver.find_elements(*LoginPageLocators.ERROR_EL_LOGIN_EMAIL)

        for el in error_elements:
            if(el.text == "Wprowadź prawidłowy adres e-mail."):
                error_is_visible = True
                break
            else:
                error_is_visible = False

        self.assertTrue(error_is_visible)

    file_path = os.path.join(CUR_DIR, '..', 'data/incorrect_password_account.csv')

    @data(*GetData.get_data(file_path))
    @unpack
    def test_incorrect_password(self, password):
        """Register with incorrect password or repassword should fail."""


        self.driver.find_element(*LoginPageLocators.LOG_IN_BTN).click()
        self.driver.find_element(*LoginPageLocators.FILL_EMAIL).send_keys("joanna@joanna.pl")
        self.driver.find_element(*LoginPageLocators.FILL_PASS).send_keys(password)
        self.driver(LoginPageLocators.SIGN_IN_BTN).submit()
        error_text = self.driver.find_element(*LoginPageLocators.ERROR_El2).text
        self.assertEqual(error_text, "DANE DOSTĘPU SĄ NIEPRAWIDŁOWE")

    def test_correct_data(self):
        """Register with correct email should be successful."""

        self.driver.find_element(*LoginPageLocators.LOG_IN_BTN).click()
        self.driver.find_element(*LoginPageLocators.FILL_EMAIL).send_keys("joanna.software.tester@gmail.com")
        self.driver.find_element(*LoginPageLocators.FILL_PASS).send_keys("Tester2020")
        self.driver.find_element(*LoginPageLocators.SIGN_IN_BTN).submit()
        user_name = self.driver.find_element(*LoginPageLocators.USER_NAME).text
        self.assertEqual(user_name, "JOANNA")
        self.driver.find_element(*LoginPageLocators.USER_NAME).click()
        self.driver(*LoginPageLocators.LOG_OUT).click()
        log_in = self.driver.find_element(*LoginPageLocators.LOG_IN_BTN).text
        self.assertEqual(log_in, "LOGOWANIE")


if __name__=="__main__":
    unittest.main(verbosity=2)








