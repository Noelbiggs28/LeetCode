import unittest
from laser_beams import Solution

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_ex1(self):
        x = self.solution.numberOfBeams(["011001","000000","010100","001000"])
        self.assertEqual(x, 8)

    def test_ex2(self):
        x = self.solution.numberOfBeams(["000","111","000"])
        self.assertEqual(x,0)

    
if __name__ == '__main__':
    unittest.main() 
    # ls laser_beams.py | entr -s "python3 -m unittest laser_beams_spec.py"