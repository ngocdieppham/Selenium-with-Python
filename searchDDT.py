import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("")
        # specify test data using @data decorator
    @data(("smartphone", 40), ("laptop", 5))
    @unpack
    def test_search(self, search_value, expected_count):
        self.search_field = self.driver.find_element(By.NAME, 'q')
        self.search_field.clear()
        self.search_field.send_keys(search_value)
        self.search_field.submit()
        
        products = self.driver.find_element(By.XPATH, '')
        # check count of products shown in results
        self.assertEqual(expected_count, len(products))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

