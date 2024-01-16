import unittest
from first_letter import Solution

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_ex1(self):
        x = self.solution.repeatedCharacter("abccbaacz")
        self.assertEqual(x, "c")

    def test_ex2(self):
        x = self.solution.repeatedCharacter("abcdd")
        self.assertEqual(x, "d")

if __name__ == '__main__':
    unittest.main()