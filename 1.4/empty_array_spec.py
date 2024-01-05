import unittest
from empty_array import Solution

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_ex1(self):
        x = self.solution.minOperations([2,3,3,2,2,4,2,3,4])
        self.assertEqual(x, 4)

    def test_ex2(self):
        x = self.solution.minOperations([2,1,2,2,3,3])
        self.assertEqual(x,-1)

    def test_ex3(self):
        x = self.solution.minOperations([19,19,19,19,19,19,19,19,19,19,19,19,19])
        self.assertEqual(x,5)

    def test_ex4(self):
        x = self.solution.minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12])
        self.assertEqual(x,7)
    
if __name__ == '__main__':
    unittest.main() 
    # ls empty_array.py | entr -s "python3 -m unittest empty_array_spec.py"