from selenium import webdriver
import unittest

class Alert(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        cls.driver.get('') # enter URL 

    def test_alert(self):
        driver = self.driver
        alert = driver.switch_to_alert()
        self.assertEqual('',alert.text) # enter text of alert to compare
        alert.accept()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
