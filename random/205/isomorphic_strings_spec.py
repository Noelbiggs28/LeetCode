import unittest
from isomorphic_strings import Solution

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_ex1(self):
        x = self.solution.isIsomorphic('egg', 'add')
        self.assertEqual(x, True)

    def test_ex2(self):
        x = self.solution.isIsomorphic('foo', 'bar')
        self.assertEqual(x, False)

    def test_ex3(self):
        x = self.solution.isIsomorphic('paper', 'title')
        self.assertEqual(x, True)

    def test_ex4(self):
        x = self.solution.isIsomorphic("bbbaaaba", "aaabbbba")
        self.assertEqual(x, False)

    def test_ex5(self):
        x = self.solution.isIsomorphic("a", "b")
        self.assertEqual(x, True)

    def test_ex6(self):
        x = self.solution.isIsomorphic("papap", "titii")
        self.assertEqual(x, False)

    def test_ex7(self):
        x = self.solution.isIsomorphic("badc", "baba")
        self.assertEqual(x, False)

if __name__ == '__main__':
    unittest.main()