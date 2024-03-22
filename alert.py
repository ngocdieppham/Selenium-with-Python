from selenium import webdriver
import unittest

class Alert(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get('') # NHẬP URL 

    def test_alert(self):
        driver = self.driver
        alert = driver.switch_to_alert()
        self.assertEqual('',alert.text)
        alert.accept()
        #alert.dismiss()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=1)