import unittest
from maxOperations import Solution

class TestMaxOperations(unittest.TestCase):
    # def testsimple(self):
    #     s = Solution()
    #     result = s.maxOperations([1, 2, 3, 4], 5)
    #     self.assertEqual(result, 2)

    def testsimple1(self):
        s = Solution()
        result = s.maxOperations([3, 1, 3, 4, 3], 6)
        self.assertEqual(result, 1)    

