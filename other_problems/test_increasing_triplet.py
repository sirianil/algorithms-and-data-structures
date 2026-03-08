import unittest
from increasing_triplet import Solution

class TestMaxOperations(unittest.TestCase):
    def testsimple(self):
        s = Solution()
        result = s.increasingTriplet([2,1,5,0,4,6])
        self.assertEqual(result, True)

    def testsimple1(self):
        s = Solution()
        result = s.increasingTriplet([5,4,3,2,1])
        self.assertEqual(result, False)