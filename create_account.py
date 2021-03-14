from selenium import webdriver
import unittest

class CreateAccounnt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        cls.driver.get('http://www.shopee.vn')
        advert_button = cls.driver.find_element_by_css_selector('div.shopee-popup__close-btn').click()

    def test_create_account(self):
        driver = self.driver
        # create_button = driver.find_element_by_link_text('LOGIN')
        create_button = driver.find_element_by_xpath("//a[@class='navbar__link navbar__link--account navbar__link--tappable navbar__link--hoverable navbar__link-text navbar__link-text--medium']")
        self.assertTrue(create_button.is_displayed() and create_button.is_enabled())
        create_button.click()
        self.assertTrue('Shopee Việt Nam | Mua và Bán Trên Ứng Dụng Di Động',driver.title)
        txt_mobile_phone = driver.find_element_by_class_name('_56AraZ')
        self.assertTrue(txt_mobile_phone.is_displayed() and txt_mobile_phone.is_enabled())
        # mobile_phone.send_keys('0799716154')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
