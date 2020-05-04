from pages.base_page import BasePage
from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def click_register_btn(self):
        el = self.driver.find_element(*LoginPageLocators.REJESTRACJA_BTN)
        el.click()

    def _verify_page(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(LoginPageLocators.REJESTRACJA_BTN))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(LoginPageLocators.REJESTRACJA_BTN))
        assert "LOGOWANIE / Rejestracja - ZARA Polska / Poland — Strona oficjalna" in self.driver.title
        print("Weryfikacja strony LoginPage")
