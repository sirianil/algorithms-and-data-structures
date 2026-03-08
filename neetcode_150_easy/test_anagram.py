import unittest
from anagram import valid_anagram

class TestAnagram(unittest.TestCase):
    def testsimple(self):
        self.assertEqual(valid_anagram("Was it a car or a cat I saw?"), False)