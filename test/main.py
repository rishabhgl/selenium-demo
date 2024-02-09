import unittest
import page
import sys

sys.path.append("../")

from utils import load_driver

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # return super().setUp()
        print("Setting the test up!")
        self.driver = load_driver(5, "http://www.python.org")

    def test_one(self):
        print("In test one-")
        assert True

    def test_two(self):
        print("In test two-")
        assert False

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()