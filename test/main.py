import unittest
from page import MainPage, SearchResultsPage
import sys
import time

sys.path.append("../")

from utils import load_driver

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # return super().setUp()
        print("Setting the test up!")
        self.driver = load_driver(5, "http://www.python.org")

    def test_search_element(self):
        main_page = MainPage(self.driver)
        assert main_page.title_matches()
        main_page.search_bar = "pycon"
        main_page.click_goto_button()
        search_results_page = SearchResultsPage(self.driver)
        assert search_results_page.found_results()


    def tearDown(self):
        time.sleep(2)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()