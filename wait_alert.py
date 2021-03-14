from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Alert(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        cls.driver.get('') # NHẬP URL 

    def test_alert(self):
        driver = self.driver
        # alert = driver.switch_to_alert()
        alert = WebDriverWait(driver,5).until(expected_conditions.alert_is_present())
        self.assertEqual('',alert.text)
        alert.accept()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)