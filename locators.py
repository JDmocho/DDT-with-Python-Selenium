from selenium.webdriver.common.by import By

class FormPageLocators():
    """ Selektory strony głównej"""
    LOG_IN_BTN = (By.XPATH, '//*[@id="header-actions"]/li[1]/a')


    """ Slektory strony logowania"""
    REGISTRATION_BTN = (By.XPATH, '//*[contains(text(),\'Utwórz konto\')]')


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
    NEWSLETTER = (By.XPATH, '//*[@id="sign-up-form"]/div[2]/div[2]/div/div[1]/label/span')
    COOKIES = (By.XPATH, '//*[@id="sign-up-form"]/div[2]/div[2]/div/div[2]/label')
    REGISTRATION = (By.ID, "sign-up-button")

    ERROR_EL = (By.CLASS_NAME, "input-tip")


class LoginPageLocators():

    LOG_IN_BTN = (By.XPATH, '//*[@id="header-actions"]/li[1]/a')
    REGISTRATION_BTN = (By.XPATH, '//*[contains(text(),\'Utwórz konto\')]')
    FILL_EMAIL = (By.NAME, 'email')
    FILL_PASS = (By.NAME, 'password')
    SIGN_IN_BTN = (By.CLASS_NAME, "logon-view__form-button")
    ERROR_EL_LOGIN_PASS = (By.CLASS_NAME, 'modal__header')
    ERROR_EL_LOGIN_EMAIL = (By.CLASS_NAME, 'form-input__error')
    ERROR_El2 = (By.XPATH, '//*[@id="theme-modal-container"]/div/div/div/div/div[1]/h1/span/span')
    ERROR_EL_LOGIN = (By.CLASS_NAME, 'form-input__error')
    SESSION_BTN = (By.LINK_TEXT, "ZALOGUJ SIĘ PONOWNIE")
    USER_NAME = (By.LINK_TEXT, "JOANNA")
    LOG_OUT = (By.LINK_TEXT, "WYLOGUJ SIĘ")


