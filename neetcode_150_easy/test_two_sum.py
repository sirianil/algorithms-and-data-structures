import unittest
from two_sum import Solution

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([5,5], 10), [0,1])
        
        self.assertEqual(sol.twoSum([4,5,6], 10), [0,2])
        