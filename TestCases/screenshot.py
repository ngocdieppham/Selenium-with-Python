from selenium import webdriver
import unittest, datetime,time
from selenium.common.exceptions import NoSuchElementException

class ScreenShot(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get('http://www.lazada.vn')

    def test_screenshot(self):
        driver = self.driver
        try:
            element = driver.find_element_by_id ('element')
        except NoSuchElementException:
            st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
            # save to directory
            file_name = 'PYTHON\chapter_9\element' + st + '.png'
            driver.get_screenshot_as_file(file_name)
            # or driver.save_screenshot(file_name)
            
            raise

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
        