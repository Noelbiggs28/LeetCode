import unittest
from max_profit import Solution

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_ex1(self):
        x = self.solution.jobScheduling([1,2,3,3],[3,4,5,6],[50,10,40,70])
        self.assertEqual(x, 120)

    def test_ex2(self):
        x = self.solution.jobScheduling([1,2,3,4,6],[3,5,10,6,9],[20,20,100,70,60])
        self.assertEqual(x,150)

    def test_ex3(self):
        x = self.solution.jobScheduling([1,1,1],[2,3,4],[5,6,4])
        self.assertEqual(x,6)

    
if __name__ == '__main__':
    unittest.main() 
    # ls *.py | entr sh -c "python3 -m unittest *spec.py"