from selenium import webdriver
import unittest

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get('http://www.lazada.vn')

    def test_search_by_category(self):
        driver=self.driver
        self.search_field = driver.find_element_by_name('q')
        self.search_field.clear()
        self.search_field.send_keys('smartphone')
        self.search_field.submit()

        self.products = driver.find_elements_by_xpath("//div[@class='_17mcb']/div")
        self.quantity = driver.find_elements_by_xpath("//div[@class=' M4pDu']")
        for item in self.quantity:
            print(item.text)
        # print('The number of smartphone per page is ' + str(len(self.products)))
        self.assertEqual(40,len(self.products))
        # for product in products:
        #   print(self.product.text)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=1)

