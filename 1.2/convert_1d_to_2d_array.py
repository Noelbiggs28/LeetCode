import unittest
from convert_1d_to_2d_array import Solution

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_ex1(self):
        x = self.solution.findContentChildren([1,2,3],[1,1])
        self.assertEqual(x, 1 )

    def test_ex2(self):
        x = self.solution.findContentChildren([1,2],[1,2,3])
        self.assertEqual(x,2)

    def test_ex3(self):
        x = self.solution.findContentChildren([1,2,3],[])
        self.assertEqual(x,0)
    
if __name__ == '__main__':
    unittest.main() 
    # ls assign_cookies.py | entr -s "python3 -m unittest cookie_spec.py"