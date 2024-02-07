import unittest
from reverse_polish import Solution

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_ex1(self):
        x = self.solution.evalRPN(tokens = ["2","1","+","3","*"])
        self.assertEqual(x, 9)

    def test_ex2(self):
        x = self.solution.evalRPN(tokens = ["4","13","5","/","+"])
        self.assertEqual(x, 6)

    def test_ex3(self):
        x = self.solution.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
        self.assertEqual(x, 22)

if __name__ == '__main__':
    unittest.main()