# -*- coding: UTF-8 -*-

"""
Test create account functionality
Version: 1.1
Author Joanna Dmochowska
"""

from tests.base_test import BaseTest
from locators import FormPageLocators
import unittest
from library import GetData
from ddt import ddt, data, unpack
import os

# Get actual DIR
CUR_DIR = os.path.dirname(os.path.abspath(__file__))


@ddt
class RegisterForm(BaseTest):
    """Testing the registration form."""

    def test_empty_registratuion_form(self):
        """Register with empty data should fail."""

        self.driver.find_element(*FormPageLocators.LOG_IN_BTN).click()
        self.driver.find_element(*FormPageLocators.REGISTRATION_BTN).click()
        self.driver.find_element(*FormPageLocators.EMAIL_INPUT).send_keys("")
        self.driver.find_element(*FormPageLocators.PASS_INPUT).send_keys("")
        self.driver.find_element(*FormPageLocators.REPASS_INPUT).send_keys("")
        self.driver.find_element(*FormPageLocators.NAME_INPUT).send_keys("")
        self.driver.find_element(*FormPageLocators.SURNAME_INPUT).send_keys("")
        self.driver.find_element(*FormPageLocators.COUNTRY_INPUT).click()
        country = self.driver.find_element(*FormPageLocators.COUNTRY_INPUT)
        country.send_keys("")
        country.click()
        self.driver.find_element(*FormPageLocators.STREET_INPUT).send_keys("")
        self.driver.find_element(*FormPageLocators.POSTCODE_INPUT).send_keys("")
        state = self.driver.find_element(*FormPageLocators.STATE_INPUT)
        state.send_keys("")
        state.click()
        self.driver.find_element(*FormPageLocators.CITY_INPUT).send_keys("")
        self.driver.find_element(*FormPageLocators.MOB1_INPUT).send_keys("")
        self.driver.find_element(*FormPageLocators.NEWSLETTER).click()
        self.driver.find_element(*FormPageLocators.COOKIES).click()
        self.driver.find_element(*FormPageLocators.REGISTRATION).submit()
        self.driver.find_element(*FormPageLocators.ERROR_EL)
        error_elements = self.driver.find_elements(*FormPageLocators.ERROR_EL)

        error_is_visible = False

        for el in error_elements:
            if el.text == "To pole jest obowiązkowe.":
                error_is_visible = True
                break
            else:
                error_is_visible = False

        self.assertTrue(error_is_visible)

    file_path = os.path.join(CUR_DIR, '..', 'data/incorrect_emails_registration.csv')

    @data(*GetData.get_data(file_path))
    @unpack
    def test_incorrect_email(self, email):
        """Register with incorrect email should fail."""

        self.driver.find_element(*FormPageLocators.LOG_IN_BTN).click()
        self.driver.find_element(*FormPageLocators.REGISTRATION_BTN).click()
        self.driver.find_element(*FormPageLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*FormPageLocators.PASS_INPUT).send_keys("CheckPassword1234!")
        self.driver.find_element(*FormPageLocators.REPASS_INPUT).send_keys("CheckPassword1234!")
        self.driver.find_element(*FormPageLocators.NAME_INPUT).send_keys("Joanna")
        self.driver.find_element(*FormPageLocators.SURNAME_INPUT).send_keys("Hejka")
        self.driver.find_element(*FormPageLocators.COUNTRY_INPUT).click()
        country = self.driver.find_element(*FormPageLocators.COUNTRY_INPUT)
        country.send_keys("Polska")
        country.click()
        self.driver.find_element(*FormPageLocators.STREET_INPUT).send_keys("Friendly")
        self.driver.find_element(*FormPageLocators.POSTCODE_INPUT).send_keys("12-345")
        self.driver.find_element(*FormPageLocators.STATE_INPUT).click()
        state = self.driver.find_element(*FormPageLocators.STATE_INPUT)
        state.send_keys("DOLNOŚLĄSKIE")
        state.click()
        self.driver.find_element(*FormPageLocators.CITY_INPUT).send_keys("WrocLove")
        self.driver.find_element(*FormPageLocators.MOB1_INPUT).send_keys("123456789")
        self.driver.find_element(*FormPageLocators.NEWSLETTER).click()
        self.driver.find_element(*FormPageLocators.COOKIES).click()
        self.driver.find_element(*FormPageLocators.REGISTRATION).submit()
        error_elements = self.driver.find_elements(*FormPageLocators.ERROR_EL)

        error_is_visible = False

        for el in error_elements:
            if el.text == "Wprowadź prawidłowy adres e-mail.":
                error_is_visible = True
                break
            else:
                error_is_visible = False

        self.assertTrue(error_is_visible)

    file_path = os.path.join(CUR_DIR, '..', 'data/incorrect_password_registration.csv')

    @data(*GetData.get_data(file_path))
    @unpack
    def test_incorect_password(self, password, repassword):
        """Register with incorect password or repassword should fail"""

        self.driver.find_element(*FormPageLocators.LOG_IN_BTN).click()
        self.driver.find_element(*FormPageLocators.REGISTRATION_BTN).click()
        self.driver.find_element(*FormPageLocators.EMAIL_INPUT).send_keys("joanna@joanna.pl")
        self.driver.find_element(*FormPageLocators.PASS_INPUT).send_keys(password)
        self.driver.find_element(*FormPageLocators.REPASS_INPUT).send_keys(repassword)
        self.driver.find_element(*FormPageLocators.NAME_INPUT).send_keys("Joanna")
        self.driver.find_element(*FormPageLocators.SURNAME_INPUT).send_keys("Hejka")
        self.driver.find_element(*FormPageLocators.COUNTRY_INPUT).click()
        country = self.driver.find_element(*FormPageLocators.COUNTRY_INPUT)
        country.send_keys("Polska")
        country.click()
        self.driver.find_element(*FormPageLocators.STREET_INPUT).send_keys("Friendly")
        self.driver.find_element(*FormPageLocators.POSTCODE_INPUT).send_keys("12-345")
        state = self.driver.find_element(*FormPageLocators.STATE_INPUT)
        state.send_keys("DOLNOŚLĄSKIE")
        state.click()
        self.driver.find_element(*FormPageLocators.CITY_INPUT).send_keys("WrocLove")
        self.driver.find_element(*FormPageLocators.MOB1_INPUT).send_keys("123456789")
        self.driver.find_element(*FormPageLocators.NEWSLETTER).click()
        self.driver.find_element(*FormPageLocators.COOKIES).click()
        self.driver.find_element(*FormPageLocators.REGISTRATION).submit()
        error_elements = self.driver.find_elements(*FormPageLocators.ERROR_EL)

        error_is_visible = False

        for el in error_elements:
            if (el.text == "Wprowadź mocne hasło: Co najmniej 8 znaków, w tym wielkie i małe litery oraz cyfry." or
                    "To pole musić być zgodne z Hasło" or "To pole jest obowiązkowe."):
                error_is_visible = True
                break
            else:
                error_is_visible = False

        self.assertTrue(error_is_visible)

    file_path = os.path.join(CUR_DIR, '..', 'data/incorrect_postcode_registration.csv')

    @data(*GetData.get_data(file_path))
    @unpack
    def test_incorect_postcode(self, postcode):
        """Register with incorect postcode should fail"""

        self.driver.find_element(*FormPageLocators.LOG_IN_BTN).click()
        self.driver.find_element(*FormPageLocators.REGISTRATION_BTN).click()
        self.driver.find_element(*FormPageLocators.EMAIL_INPUT).send_keys("joanna@joanna.pl")
        self.driver.find_element(*FormPageLocators.PASS_INPUT).send_keys("CheckPassword1234!")
        self.driver.find_element(*FormPageLocators.REPASS_INPUT).send_keys("CheckPassword1234!")
        self.driver.find_element(*FormPageLocators.NAME_INPUT).send_keys("Joanna")
        self.driver.find_element(*FormPageLocators.SURNAME_INPUT).send_keys("Hejka")
        self.driver.find_element(*FormPageLocators.COUNTRY_INPUT).click()
        country = self.driver.find_element(*FormPageLocators.COUNTRY_INPUT)
        country.send_keys("Polska")
        country.click()
        self.driver.find_element(*FormPageLocators.STREET_INPUT).send_keys("Friendly")
        self.driver.find_element(*FormPageLocators.POSTCODE_INPUT).send_keys(postcode)
        self.driver.find_element(*FormPageLocators.STATE_INPUT).click()
        state = self.driver.find_element(*FormPageLocators.STATE_INPUT)
        state.send_keys("DOLNOŚLĄSKIE")
        state.click()
        self.driver.find_element(*FormPageLocators.CITY_INPUT).send_keys("WrocLove")
        self.driver.find_element(*FormPageLocators.MOB1_INPUT).send_keys("123456789")
        self.driver.find_element(*FormPageLocators.NEWSLETTER).click()
        self.driver.find_element(*FormPageLocators.COOKIES).click()
        self.driver.find_element(*FormPageLocators.REGISTRATION).submit()
        self.driver.find_element(*FormPageLocators.ERROR_EL)
        error_elements = self.driver.find_elements(*FormPageLocators.ERROR_EL)

        error_is_visible = False

        for el in error_elements:
            if el.text == "Wartość nieprawidłowa, prosimy o sprawdzenie formatu":
                error_is_visible = True
                break
            else:
                error_is_visible = False

        self.assertTrue(error_is_visible)

    file_path = os.path.join(CUR_DIR, '..', 'data/incorrect_city_registration.csv')

    @data(*GetData.get_data(file_path))
    @unpack
    def test_incorect_city(self, city):
        """Register with incorect city should fail"""

        self.driver.find_element(*FormPageLocators.LOG_IN_BTN).click()
        self.driver.find_element(*FormPageLocators.REGISTRATION_BTN).click()
        self.driver.find_element(*FormPageLocators.EMAIL_INPUT).send_keys("joanna@joanna.pl")
        self.driver.find_element(*FormPageLocators.PASS_INPUT).send_keys("CheckPassword1234!")
        self.driver.find_element(*FormPageLocators.REPASS_INPUT).send_keys("CheckPassword1234!")
        self.driver.find_element(*FormPageLocators.NAME_INPUT).send_keys("Joanna")
        self.driver.find_element(*FormPageLocators.SURNAME_INPUT).send_keys("Hejka")
        country = self.driver.find_element(*FormPageLocators.COUNTRY_INPUT)
        country.send_keys("Polska")
        country.click()
        self.driver.find_element(*FormPageLocators.STREET_INPUT).send_keys("Friendly")
        self.driver.find_element(*FormPageLocators.POSTCODE_INPUT).send_keys("12-345")
        self.driver.find_element(*FormPageLocators.STATE_INPUT).click()
        state = self.driver.find_element(*FormPageLocators.STATE_INPUT)
        state.send_keys("DOLNOŚLĄSKIE")
        state.click()
        self.driver.find_element(*FormPageLocators.CITY_INPUT).send_keys(city)
        self.driver.find_element(*FormPageLocators.MOB1_INPUT).send_keys("123456789")
        self.driver.find_element(*FormPageLocators.NEWSLETTER).click()
        self.driver.find_element(*FormPageLocators.COOKIES).click()
        self.driver.find_element(*FormPageLocators.REGISTRATION).submit()
        self.driver.find_element(*FormPageLocators.ERROR_EL)
        error_elements = self.driver.find_elements(*FormPageLocators.ERROR_EL)

        error_is_visible = False

        for el in error_elements:
            if el.text == "Wartość nieprawidłowa, prosimy o sprawdzenie formatu":
                error_is_visible = True
                break
            else:
                error_is_visible = False

        self.assertTrue(error_is_visible)

    file_path = os.path.join(CUR_DIR, '..', 'data/incorrect_phone_registration.csv')

    @data(*GetData.get_data(file_path))
    @unpack
    def test_incorect_phone(self, phone):
        """Register with incorect phone should fail"""

        self.driver.find_element(*FormPageLocators.LOG_IN_BTN).click()
        self.driver.find_element(*FormPageLocators.REGISTRATION_BTN).click()
        self.driver.find_element(*FormPageLocators.EMAIL_INPUT).send_keys("joanna@joanna.pl")
        self.driver.find_element(*FormPageLocators.PASS_INPUT).send_keys("CheckPassword1234!")
        self.driver.find_element(*FormPageLocators.REPASS_INPUT).send_keys("CheckPassword1234!")
        self.driver.find_element(*FormPageLocators.NAME_INPUT).send_keys("Joanna")
        self.driver.find_element(*FormPageLocators.SURNAME_INPUT).send_keys("Hejka")
        self.driver.find_element(*FormPageLocators.COUNTRY_INPUT).click()
        country = self.driver.find_element(*FormPageLocators.COUNTRY_INPUT)
        country.send_keys("Polska")
        country.click()
        self.driver.find_element(*FormPageLocators.STREET_INPUT).send_keys("Friendly")
        self.driver.find_element(*FormPageLocators.POSTCODE_INPUT).send_keys("12-345")
        self.driver.find_element(*FormPageLocators.STATE_INPUT).click()
        state = self.driver.find_element(*FormPageLocators.STATE_INPUT)
        state.send_keys("DOLNOŚLĄSKIE")
        state.click()
        self.driver.find_element(*FormPageLocators.CITY_INPUT).send_keys("WrocLove")
        self.driver.find_element(*FormPageLocators.MOB1_INPUT).send_keys(phone)
        self.driver.find_element(*FormPageLocators.NEWSLETTER).click()
        self.driver.find_element(*FormPageLocators.COOKIES).click()
        self.driver.find_element(*FormPageLocators.REGISTRATION).submit()
        self.driver.find_element(*FormPageLocators.ERROR_EL)
        error_elements = self.driver.find_elements(*FormPageLocators.ERROR_EL)

        error_is_visible = False

        for el in error_elements:
            if el.text == "Podaj prawidłowy numer telefonu":
                error_is_visible = True
                break
            else:
                error_is_visible = False

        self.assertTrue(error_is_visible)


if __name__ == "__main__":
    unittest.main(verbosity=2)
