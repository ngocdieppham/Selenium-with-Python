import unittest
from xmlrunner import xmlrunner

from searchtests import SearchTests
from homepagetest import HomePageTest

search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
smoke_test = unittest.TestSuite([search_test,home_page_test])
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_test)