from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Alert(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get('') # ENTER URL 

    def test_alert(self):
        driver = self.driver
        alert = WebDriverWait(driver,5).until(expected_conditions.alert_is_present())
        self.assertEqual('',alert.text)
        alert.accept()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=1)