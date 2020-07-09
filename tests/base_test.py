import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    """Base test class"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.zara.com/pl/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.delete_all_cookies()

    def tearDown(self):
        self.driver.quit()
