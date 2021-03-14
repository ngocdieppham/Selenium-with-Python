from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Wait(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        cls.driver.get('http://www.lazada.vn')

    def test_login_link(self):
        driver = self.driver
        # login_button = driver.find_element_by_link_text('LOGIN')
        # explicit_wait là chờ đợi trong 1 khoảng thời gian đi kèm với 1 điều kiện
        login_button = WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'LOGIN')))
        login_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
