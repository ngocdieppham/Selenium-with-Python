from selenium import webdriver
import unittest

class SelectLanguage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        cls.driver.get('') # ENTER URL  

    def test_language_option(self):
        exp_option = ['VietNam','English','France']
        act_option = []
        select_language = self.driver.find_element_by_id('select_language')
        self.assertEqual(3,len(select_language.options))

        for option in select_language.options:
            act_option.append(option.text)

        # assert 2 List
        self.assertListEqual(exp_option,act_option) 
        # assert choosing default language
        self.assertEqual('English',select_language.first_selected_option.text)
        # choose another language
        select_language.select_by_visible_text('France')
        # check chosen language in url ?
        self.assertTrue('store=France' in self.driver.current_url)
        # refresh page after choosing new language
        # choose select tag again
        select_language = self.driver.find_element_by_id('select_language')
        # choose language by index
        select_language.select_by_index(0)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)