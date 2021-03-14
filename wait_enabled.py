import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class WaitEnabled(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        cls.driver.get('http://www.lazada.vn')
        WebDriverWait(cls.driver,3).until(expected_conditions.title_contains('Shopping online - Buy online on Lazada.vn'))

    def test_account(self):
        driver = self.driver
        login_button = WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,'LOGIN')))
        login_button.click()
        WebDriverWait(driver,3).until(expected_conditions.title_contains('Lazada.vn: Online Shopping Vietnam'))
        create_button = WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,'SIGNUP')))
        create_button.click()
        self.assertEqual('Create your Lazada Account',driver.find_element_by_xpath("//h3[contains(text(),'Create your Lazada Account')]").text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)