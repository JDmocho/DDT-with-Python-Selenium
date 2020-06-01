#import Classes
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

#import rest stuff
from library import GetData
import unittest
import csv
from ddt import ddt, data, unpack
import os




@ddt
class RegistrationPrivateTest(BaseTest):  #dziedziczymy z klasy BaseTest
    """
    Testy rejestracji
    W niektórych testach celowo wprowadzamy błędny adres email w celu uniknięcia rejestracji na stronie

    """
    # Get actual DIR
    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(CUR_DIR, '..', 'data/bad_emails.csv')

    @data(*GetData.get_data(file_path))
    @unpack

    def test_incorrect_email(self,email,password,repassword,name,surname,country,street,postcode,state,city,mob1):
        """
        test_incorrect_email - testuje tylko pole email, reszta danych prawidłowa

        Dopuszczalne wartości:
        - Długość: 6-255
        - Dozwolone znaki: A-Z, a-z, 0-9 oraz "@",".","-","_"
        """

        #Tworzymy nowy obiekt HomePage
        hp = HomePage(self.driver)
        #Używamy metody click_zaloguj_btn
        hp.click_zaloguj_btn()

        lp = LoginPage(self.driver)
        lp.click_register_btn()

        rp = RegisterPage(self.driver)
        rp.fill_email(email)
        rp.fill_password(password)
        rp.fill_repassword(password)
        rp.fill_name(name)
        rp.fill_surname(surname)
        rp.choose_country(country)
        rp.choose_state(state)
        rp.fill_street(street)
        rp.fill_postcode(postcode)
        rp.fill_city(city)
        rp.fill_mob1(mob1)
        rp.accepts()
        rp.submit()

        rp.verify_visible_errors(1, ["Wprowadź prawidłowy adres e-mail."])



    file_path = os.path.join(CUR_DIR, '..', 'data/bad_password_repassword.csv')

    @data(*GetData.get_data(file_path))
    @unpack

    def test_password_repassword(self,email,password,repassword,name,surname,country,street,postcode,state,city,mob1):
        """
        test_password_repassword - testuje pola password i repassword, reszta danych prawidłowa

        Dopuszczalne wartości:
        - Długość: 8-255
        - Dozwolone znaki: brak ograniczeń
        - Dodatkowe wymogi: 8 znaków, w tym wielkie i małe litery oraz cyfry, pole repassowrd identyczne jak password
        """
        #Tworzymy nowy obiekt HomePage
        hp = HomePage(self.driver)
        #Używamy metody click_zaloguj_btn
        hp.click_zaloguj_btn()

        lp = LoginPage(self.driver)
        lp.click_register_btn()

        rp = RegisterPage(self.driver)
        rp.fill_email(email)
        rp.fill_password(password)
        rp.fill_repassword(password)
        rp.fill_name(name)
        rp.fill_surname(surname)
        rp.choose_country(country)
        rp.choose_state(state)
        rp.fill_street(street)
        rp.fill_postcode(postcode)
        rp.fill_city(city)
        rp.fill_mob1(mob1)
        rp.accepts()
        rp.submit()

        rp.verify_visible_errors(2, ["Wprowadź mocne hasło: Co najmniej 8 znaków, w tym wielkie i małe litery oraz cyfry.","To pole musić być zgodne z Hasło"])

    file_path = os.path.join(CUR_DIR, '..', 'data/bad_name_surname.csv')

    @data(*GetData.get_data(file_path))
    @unpack

    def test_name_surname(self,email,password,repassword,name,surname,country,street,postcode,state,city,mob1):
        """
        test_name_surname - testuje pola imie i nazwisko, reszta danych prawidłowa (opórcz email)

        Dopuszczalne wartości:
        - Długość: 2-255
        - Dozwolone znaki: A-Z, a-z, znaki diakrytyczne
        """
        #Tworzymy nowy obiekt HomePage
        hp = HomePage(self.driver)
        #Używamy metody click_zaloguj_btn
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.click_register_btn()
        rp = RegisterPage(self.driver)
        rp.fill_email(email)
        rp.fill_password(password)
        rp.fill_repassword(password)
        rp.fill_name(name)
        rp.fill_surname(surname)
        rp.choose_country(country)
        rp.choose_state(state)
        rp.fill_street(street)
        rp.fill_postcode(postcode)
        rp.fill_city(city)
        rp.fill_mob1(mob1)
        rp.accepts()
        rp.submit()

        rp.verify_visible_errors(3, ["Wprowadź prawidłowy adres e-mail.","Wprowadź prawidłowe dane","Wprowadź prawidłowe dane"])


    file_path = os.path.join(CUR_DIR, '..', 'data/bad_adres.csv')

    @data(*GetData.get_data(file_path))
    @unpack

    def test_adres(self,email,password,repassword,name,surname,country,street,postcode,state,city,mob1):
        """
        test_adres - testuje pole adres, reszta danych prawidłowa (opórcz email)

        Dopuszczalne wartości:
        - Długość: 2-255
        - Dozwolone znaki: A-Z, a-z, 0-9, ".", ",", znaki diakrytyczne
        """
        #Tworzymy nowy obiekt HomePage
        hp = HomePage(self.driver)
        #Używamy metody click_zaloguj_btn
        hp.click_zaloguj_btn()

        lp = LoginPage(self.driver)
        lp.click_register_btn()

        rp = RegisterPage(self.driver)
        rp.fill_email(email)
        rp.fill_password(password)
        rp.fill_repassword(password)
        rp.fill_name(name)
        rp.fill_surname(surname)
        rp.choose_country(country)
        rp.choose_state(state)
        rp.fill_street(street)
        rp.fill_postcode(postcode)
        rp.fill_city(city)
        rp.fill_mob1(mob1)
        rp.accepts()
        rp.submit()


        rp.verify_visible_errors(2, ["Wprowadź prawidłowy adres e-mail.","Wprowadź prawidłowe dane"])

    file_path = os.path.join(CUR_DIR, '..', 'data/bad_post_code.csv')

    @data(*GetData.get_data(file_path))
    @unpack


    def test_postcode(self,email,password,repassword,name,surname,country,street,postcode,state,city,mob1):
        """
        test_postcode - testuje pole kod pocztowy, reszta danych prawidłowa

        Dopuszczalne wartości:
        - Długość: 6
        - Dozwolone znaki: 0-9, "-"
        """
        #Tworzymy nowy obiekt HomePage
        hp = HomePage(self.driver)
        #Używamy metody click_zaloguj_btn
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.click_register_btn()
        rp = RegisterPage(self.driver)
        rp.fill_email(email)
        rp.fill_password(password)
        rp.fill_repassword(password)
        rp.fill_name(name)
        rp.fill_surname(surname)
        rp.choose_country(country)
        rp.choose_state(state)
        rp.fill_street(street)
        rp.fill_postcode(postcode)
        rp.fill_city(city)
        rp.fill_mob1(mob1)
        rp.accepts()
        rp.submit()

        rp.verify_visible_errors(1, ["Wpisana wartość jest nieprawidłowa. Prosimy o sprawdzenie formatu"])

    file_path = os.path.join(CUR_DIR, '..', 'data/bad_city.csv')

    @data(*GetData.get_data(file_path))
    @unpack

    def test_city(self,email,password,repassword,name,surname,country,street,postcode,state,city,mob1):
        """
        test_city - testuje pole miasto, reszta danych prawidłowa (opórcz email)

        Dopuszczalne wartości:
        - Długość: 2-255
        - Dozwolone znaki: A-Z, a-z, znaki diakrytyczne
        """
        #Tworzymy nowy obiekt HomePage
        hp = HomePage(self.driver)
        #Używamy metody click_zaloguj_btn
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.click_register_btn()
        rp = RegisterPage(self.driver)
        rp.fill_email(email)
        rp.fill_password(password)
        rp.fill_repassword(password)
        rp.fill_name(name)
        rp.fill_surname(surname)
        rp.choose_country(country)
        rp.choose_state(state)
        rp.fill_street(street)
        rp.fill_postcode(postcode)
        rp.fill_city(city)
        rp.fill_mob1(mob1)
        rp.accepts()
        rp.submit()

        rp.verify_visible_errors(2, ["Wprowadź prawidłowy adres e-mail.","Wprowadź prawidłowe dane"])


    file_path = os.path.join(CUR_DIR, '..', 'data/bad_phone.csv')

    @data(*GetData.get_data(file_path))
    @unpack

    def test_phone(self,email,password,repassword,name,surname,country,street,postcode,state,city,mob1):
        """
        test_phone - testuje pole telefon, reszta danych prawidłowa

        Dopuszczalne wartości:
        - Długość: 9
        - Dozwolone znaki: 0-9
        """
        #Tworzymy nowy obiekt HomePage
        hp = HomePage(self.driver)
        #Używamy metody click_zaloguj_btn
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.click_register_btn()
        rp = RegisterPage(self.driver)
        rp.fill_email(email)
        rp.fill_password(password)
        rp.fill_repassword(password)
        rp.fill_name(name)
        rp.fill_surname(surname)
        rp.choose_country(country)
        rp.choose_state(state)
        rp.fill_street(street)
        rp.fill_postcode(postcode)
        rp.fill_city(city)
        rp.fill_mob1(mob1)
        rp.accepts()
        rp.submit()

        rp.verify_visible_errors(2, ["Wprowadź prawidłowy adres e-mail.","Podaj prawidłowy numer telefonu"])



    def test_empty_fill(self):
        """
        empty_fill - testuje formularz pod kątem pustych danych

        """
        #Tworzymy nowy obiekt HomePage
        hp = HomePage(self.driver)
        #Używamy metody click_zaloguj_btn
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.click_register_btn()
        rp = RegisterPage(self.driver)
        rp.fill_email("")
        rp.fill_password("")
        rp.fill_repassword("")
        rp.fill_name("")
        rp.fill_surname("")
        rp.choose_country("")
        rp.choose_state("")
        rp.fill_street("")
        rp.fill_postcode("")
        rp.fill_city("")
        rp.fill_mob1("")
        rp.accepts()
        rp.submit()

        rp.verify_visible_errors(10, ["To pole jest obowiązkowe.","To pole jest obowiązkowe.","To pole jest obowiązkowe.","To pole jest obowiązkowe.","To pole jest obowiązkowe.","To pole jest obowiązkowe.","To pole jest obowiązkowe.","To pole jest obowiązkowe.","To pole jest obowiązkowe.","To pole jest obowiązkowe."])

if __name__=="__main__":
    unittest.main(verbosity=2)
