import unittest
from HTMLTestRunner import HTMLTestRunner
import os

from searchtests import SearchTests
from homepagetest import HomePageTest

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

# xuất nội dung outfile TestReport.html trong terminal
# if __name__=='__main__':
    # HTMLTestRunner.main()