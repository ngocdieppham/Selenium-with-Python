from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get('') # enter url of website

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME,'')) 
    
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID,''))
    
    def test_shopping_cart_empty_message(self):
        shopping_cart_icon = self.driver.find_element_by_class_name('')
        shopping_cart_icon.click()
        shopping_cart_status = self.driver.find_element_by_class_name('').text
        self.assertTrue('',shopping_cart_status)
        close_cart = self.driver.find_element_by_class_name('').click()
    
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
    
    def is_element_present(self,how,what):
        """
        Utility method to check presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try: self.driver.find_element(by=how,value=what)
        except NoSuchElementException as e:return False 
        return True

if __name__=='__main__':
    unittest.main(verbosity=3)
