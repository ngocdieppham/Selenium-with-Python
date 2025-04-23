import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() # create a new Chrome session
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get() # enter the URL and navigate to that page

    def tearDown(self):
        self.driver.quit() # close the browser window