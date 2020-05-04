from selenium.webdriver.common.by import By

class HomePageLocators():
    """ Selektory strony głównej"""
    ZALOGUJ_BTN = (By.XPATH, '//*[@id="header-actions"]/li[1]/a')

class LoginPageLocators():
    """ Slektory strony logowania"""
    REJESTRACJA_BTN = (By.XPATH, '//*[@id="main"]/article/div/section[2]/button')



class FormPageLocators():
    COMPANY = (By.XPATH, '//*[@id="user-type-radios"]/fieldset/ul/li[2]/label/span[1]')
    PRIVATE = (By.XPATH, '//*[@id="user-type-radios"]/fieldset/ul/li[1]/label/span[1]')
    EMAIL_INPUT = (By.NAME, 'email')
    PASS_INPUT = (By.NAME, 'password')
    REPASS_INPUT = (By.NAME, 'passRepeat')
    NAME_INPUT = (By.NAME, 'firstName')
    SURNAME_INPUT = (By.NAME, 'lastName')
    COUNTRY_INPUT = (By.NAME, 'country')
    STREET_INPUT = (By.NAME, 'address1')
    POSTCODE_INPUT = (By.ID, 'zip-code')
    STATE_INPUT = (By.NAME, 'stateCode')
    CITY_INPUT = (By.NAME, 'city')
    MOB1_INPUT = (By.NAME, 'phone1')
    AGREE1 = (By.XPATH, '//*[@id="sign-up-form"]/div[2]/div[2]/div/div[2]/label')
    SUBMIT = (By.ID, 'sign-up-button')
    REGISTRATION_ERRORS = (By.XPATH, '//span[contains(@class, "input-tip visible")]')
