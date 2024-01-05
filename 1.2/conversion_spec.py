import unittest
from convert_1d_to_2d_array import Solution

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_ex1(self):
        x = self.solution.findMatrix([1,3,4,1,2,3,1])
        self.assertEqual(x, [[1,3,4,2],[1,3],[1]])

    def test_ex2(self):
        x = self.solution.findMatrix([1,2,3,4])
        self.assertEqual(x,[[4,3,2,1]])

    
if __name__ == '__main__':
    unittest.main() 
    # ls convert_1d_to_2d_array.py | entr -s "python3 -m unittest conversion_spec.py"