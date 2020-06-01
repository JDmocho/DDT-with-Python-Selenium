from pages.base_page import BasePage
from locators import FormPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage(BasePage):

    def wait_for_elements(self, element):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(element))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(element))

    def fill_email(self, email):
        self.wait_for_elements(FormPageLocators.EMAIL_INPUT)
        el = self.driver.find_element(*FormPageLocators.EMAIL_INPUT)
        el.send_keys(email)

    def fill_password(self, password):
        self.wait_for_elements(FormPageLocators.PASS_INPUT)
        el = self.driver.find_element(*FormPageLocators.PASS_INPUT)
        el.send_keys(password)

    def fill_repassword(self, repassword):
        self.wait_for_elements(FormPageLocators.REPASS_INPUT)
        el = self.driver.find_element(*FormPageLocators.REPASS_INPUT)
        el.send_keys(repassword)

    def fill_name(self, name):
        self.wait_for_elements(FormPageLocators.NAME_INPUT)
        el = self.driver.find_element(*FormPageLocators.NAME_INPUT)
        el.send_keys(name)

    def fill_surname(self, surname):
        self.wait_for_elements(FormPageLocators.SURNAME_INPUT)
        el = self.driver.find_element(*FormPageLocators.SURNAME_INPUT)
        el.send_keys(surname)

    def choose_country(self, country):
        self.wait_for_elements(FormPageLocators.COUNTRY_INPUT)
        self.driver.find_element(*FormPageLocators.COUNTRY_INPUT).click()
        self.driver.find_element(*FormPageLocators.COUNTRY_INPUT).send_keys(country)


    def fill_street(self, street):
        self.wait_for_elements(FormPageLocators.STREET_INPUT)
        el = self.driver.find_element(*FormPageLocators.STREET_INPUT)
        el.send_keys(street)

    def fill_postcode(self, postcode):
        self.wait_for_elements(FormPageLocators.POSTCODE_INPUT)
        el = self.driver.find_element(*FormPageLocators.POSTCODE_INPUT)
        el.send_keys(postcode)

    def choose_state(self, state):
        self.wait_for_elements(FormPageLocators.STATE_INPUT)
        el = self.driver.find_element(*FormPageLocators.STATE_INPUT)
        el.send_keys(state)

    def fill_city(self, city):
        self.wait_for_elements(FormPageLocators.CITY_INPUT)
        el = self.driver.find_element(*FormPageLocators.CITY_INPUT)
        el.send_keys(city)

    def fill_mob1(self, mob1):
        self.wait_for_elements(FormPageLocators.MOB1_INPUT)
        self.driver.find_element(*FormPageLocators.MOB1_INPUT).send_keys(mob1)

    def accepts(self):
        self.wait_for_elements(FormPageLocators.AGREE1)
        self.driver.find_element(*FormPageLocators.AGREE1).click()

    def submit(self):
        self.wait_for_elements(FormPageLocators.SUBMIT)
        self.driver.find_element(*FormPageLocators.SUBMIT).click()

    def verify_visible_errors(self, number_of_errors, errors_texts):
        error_notices = self.driver.find_elements(*FormPageLocators.REGISTRATION_ERRORS)
        visible_error_notices = []
        # Zapisuję widoczne błędy do listy visible_error_notices
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        # Sprawdzam, czy widoczna jest właściwa liczba błędów
        print("visible_error_notices ",len(visible_error_notices))
        print("number_of_errors ",number_of_errors)
        assert len(visible_error_notices) == number_of_errors
        # Sprawdzam treść widocznych błędów
        errors_text_fact = []
        for i in range(len(visible_error_notices)):
            errors_text_fact.append(visible_error_notices[i].get_attribute("innerText") )
        print("Bledy na stronie: ", errors_text_fact)
        print("Bledy zakladane: ", errors_texts)
        assert errors_text_fact == errors_texts
