import unittest
from two_halves import Solution

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_ex1(self):
        x = self.solution.halvesAreAlike("book")
        self.assertEqual(x, True)

    def test_ex2(self):
        x = self.solution.halvesAreAlike("textbook")
        self.assertEqual(x,False)



    
if __name__ == '__main__':
    unittest.main() 
    # ls *.py | entr sh -c "python3 -m unittest *spec.py"