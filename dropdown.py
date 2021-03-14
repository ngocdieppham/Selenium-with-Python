from selenium import webdriver
import unittest

class SelectLanguage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        cls.driver.get('') # NHẬP URL CỦA WEBSITE 

    def test_language_option(self):
        exp_option = ['VietNam','English','France']
        act_option = []
        select_language = self.driver.find_element_by_id('select_language')
        self.assertEqual(3,len(select_language.options))

        for option in select_language.options:
            act_option.append(option.text)

        # so sánh 2 List
        self.assertListEqual(exp_option,act_option) 
        # so sánh lựa chọn ngôn ngữ đầu tiên mặc định
        self.assertEqual('English',select_language.first_selected_option.text)
        # chọn ngôn ngữ khác
        select_language.select_by_visible_text('France')
        # check url có ngôn ngữ đã chọn hay chưa ?
        self.assertTrue('store=France' in self.driver.current_url)
        # sau khi chon ngôn ngữ mới sẽ refesh lại trang
        # cần chọn lại thẻ select
        select_language = self.driver.find_element_by_id('select_language')
        # chọn ngôn ngữ bằng chỉ mục
        select_language.select_by_index(0)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)