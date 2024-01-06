import unittest
from longest_sub import Solution

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_ex1(self):
        x = self.solution.lengthOfLIS([10,9,2,5,3,7,101,18])
        self.assertEqual(x, 4)

    def test_ex2(self):
        x = self.solution.lengthOfLIS([0,1,0,3,2,3])
        self.assertEqual(x,4)

    def test_ex3(self):
        x = self.solution.lengthOfLIS([7,7,7,7,7,7,7])
        self.assertEqual(x,1)

    
if __name__ == '__main__':
    unittest.main() 
    # ls *.py | entr sh -c "python3 -m unittest *spec.py"