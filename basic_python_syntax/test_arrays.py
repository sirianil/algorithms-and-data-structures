import unittest
from arrays import binary_search, merge_sort

class TestBinarySearch(unittest.TestCase):
    def tests(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 4), True)

        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], -4), False)

        self.assertEqual(binary_search([1], 1), True)

        self.assertEqual(binary_search([], 1), False)

        self.assertEqual(binary_search([-19, -10, -5, -4, -1, 0, 10], 1), False)

        self.assertEqual(binary_search([-19, -10, -5, -4, -1, 0, 10], -1), True)

class TestMergeSort(unittest.TestCase):
    def tests(self):
        self.assertEqual(merge_sort([10, 11, 1,2]), [1, 2, 10, 11])

        self.assertEqual(merge_sort([10, 1, 0, 1, 1, -3, -14]), [-14, -3, 0, 1, 1, 1, 10])

        self.assertEqual(merge_sort([20, 10]), [10, 20])

        self.assertEqual(merge_sort([]), [])

        self.assertEqual(merge_sort([-1]), [-1])

        self.assertEqual(merge_sort([-1, -1]), [-1, -1])