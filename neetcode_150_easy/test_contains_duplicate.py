import unittest 
from contains_duplicate import contains_duplicate

class ContainsDupTest(unittest.TestCase):
    def test_unit(self):
        self.assertEqual(contains_duplicate([1, 5, 5, 9, 10], 5), True)

        self.assertEqual(contains_duplicate([1, 5, 5, 9, 10], 15), False)

        self.assertEqual(contains_duplicate([], 5), False)
