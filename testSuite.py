import unittest

from searchTest import SearchTests
from homepageTest import HomePageTest

search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
smoke_test = unittest.TestSuite([search_test,home_page_test])
unittest.TextTestRunner(verbosity=2).run(smoke_test)