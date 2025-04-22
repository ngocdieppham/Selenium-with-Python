import unittest
from HTMLTestRunner import HTMLTestRunner
import os

from searchTest import SearchTests
from homepageTest import HomePageTest

dir = os.getcwd()

search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
smoke_test = unittest.TestSuite([search_test,home_page_test])

outfile = open(dir + '\TestReport.html','w')

runner = HTMLTestRunner.HTMLTestRunner(
    stream = outfile,
    title = 'TEST REPORT',
    description = 'SMOKE TEST'
)
runner.run(smoke_test)

# export content of outfile TestReport.html into terminal
# if __name__=='__main__':
    # HTMLTestRunner.main()