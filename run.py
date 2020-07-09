import unittest
from tests.register_form import RegisterForm

# Pobierz test, które chcesz uruchomić
registration_test_1 = unittest.TestLoader().loadTestsFromTestCase(RegisterForm)


# Stwórz Test Suita
test_suite = unittest.TestSuite([registration_test_1])

# odpal
unittest.TextTestRunner(verbosity=2).run(test_suite)
