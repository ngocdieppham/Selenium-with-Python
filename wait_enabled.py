import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class WaitEnabled(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get('https://www.lazada.vn/')
        WebDriverWait(self.driver,3).until(expected_conditions.title_contains('Lazada - Mua Sắm Hàng Chất Giá Tốt Online'))

    def test_account(self):
        driver = self.driver
        #check LOGIN is clickable
        login_button = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,'LOGIN')))
        login_button.click()
        self.assertEqual('Welcome to Lazada! Please login.',driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/h3').text)
        #check SIGNUP is clickable
        create_button = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,'SIGNUP')))
        create_button.click()
        self.assertEqual('Create your Lazada Account',driver.find_element_by_xpath("//*[@id='container']/div/div[1]/h3").text)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=1)