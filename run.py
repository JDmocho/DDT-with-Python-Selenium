import unittest
from tests.register_private_page_test import RegistrationPrivateTest
#from tests.register_company_page_test import LoginPageTest
#from tests.register_private_page_test import CartPageTest


# Pobierz testy, które chcesz uruchomić
registration_test_1 = unittest.TestLoader().loadTestsFromTestCase(RegistrationPrivateTest)
#registration_test_2 = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)
#registration_test_3 = unittest.TestLoader().loadTestsFromTestCase(CartPageTest)

# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([registration_test_1])

# odpal
unittest.TextTestRunner(verbosity=2).run(test_suite)
