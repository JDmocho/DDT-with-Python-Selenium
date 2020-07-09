import unittest
from tests.register_form import RegisterForm

# Load tests from test sase
registration_test_1 = unittest.TestLoader().loadTestsFromTestCase(RegisterForm)


# Create TestSuite
test_suite = unittest.TestSuite([registration_test_1])

# Run
unittest.TextTestRunner(verbosity=2).run(test_suite)
