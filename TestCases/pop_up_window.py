from selenium import webdriver
import unittest

class PopUpWindowTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get('') # enter URL

    def test_pop_up_window(self):
        driver=self.driver
        # save windowhandle - Parent Browser Window into a variable
        parrent_window = driver.current_window_handle
        # open pop_up window or child window
        btn_help = driver.find_element_by_id('helpbutton')
        btn_help.click()
        driver.switch_to_window('HelpWindow')
        driver.close()
        driver.switch_to_window(parrent_window)
       

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=1)

