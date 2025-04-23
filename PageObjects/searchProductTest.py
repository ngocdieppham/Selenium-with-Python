import unittest
from ..TestCases.homepageTest import HomePageTest
from baseTestCase import BaseTestCase

class SearchProductTest(BaseTestCase):
    def testSearchForProduct(self):
        homepage = HomePageTest(self.driver)
        search_results = homepage.search.searchFor('smartphone')
        self.assertEqual(40, search_results.product_count)
        product = search_results.open_product_page('')
        self.assertEqual('', product.name)
        self.assertEqual('', product.price)

if __name__=='__main__':
    unittest.main(verbosity=2)