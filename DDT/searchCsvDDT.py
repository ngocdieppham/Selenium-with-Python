import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    data_file = open(file_name, 'rb')
    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader, None)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows

@ddt
class SearchCsvDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://lazada.vn')

    """get data from specified csv file
    by calling get_data method"""
    @data(*get_data("testdata.csv"))
    @unpack

    def test_search(self, search_value, expected_count):
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = self.driver.find_element(By.XPATH,'')
        if int(expected_count) > 0:
            self.assertEqual(int(expected_count), len(products))
        else:
            raise "Expected count must been larger than zero"
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()