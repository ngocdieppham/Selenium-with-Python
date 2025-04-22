from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Wait(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get('') #enter URL

    def test_login_link(self):
        driver = self.driver
        # explicit_wait is to wait for a period of time with a condition
        # WebDriver provide WebDriverWait method and expected_conditions class
        login_button = WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'LOGIN')))
        login_button.click()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=1)
