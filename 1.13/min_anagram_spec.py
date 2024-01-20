import unittest
from min_anagram import Solution

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_ex1(self):
        x = self.solution.minSteps("bab", "aba")
        self.assertEqual(x, 1)

    def test_ex2(self):
        x = self.solution.minSteps("leetcode", "practice")
        self.assertEqual(x,5)

    def test_ex3(self):
        x = self.solution.minSteps("anagram", "mangaar")
        self.assertEqual(x,0)
    
    def test_ex4(self):
        x = self.solution.minSteps("friend", "family")
        self.assertEqual(x,4)

    def test_ex5(self):
        x = self.solution.minSteps("gctcxyuluxjuxnsvmomavutrrfb", "qijrjrhqqjxjtprybrzpyfyqtzf")
        self.assertEqual(x,18)

if __name__ == '__main__':
    unittest.main() 