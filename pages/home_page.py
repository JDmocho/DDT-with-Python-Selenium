from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators

class HomePage(BasePage):

    def click_zaloguj_btn(self):
        el = self.driver.find_element(*HomePageLocators.ZALOGUJ_BTN)
        el.click()

    def _verify_page(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.ZALOGUJ_BTN))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(HomePageLocators.ZALOGUJ_BTN))
        assert "ZARA Polska / Poland | Nowa Kolekcja Online" in self.driver.title
        print("Weryfikacja strony HomePage")
