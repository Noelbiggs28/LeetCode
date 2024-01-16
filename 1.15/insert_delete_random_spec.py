import unittest
from insert_delete_random import RandomizedSet

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.solution = RandomizedSet()

    def test_insert1(self):
        x = self.solution.insert(1)
        self.assertEqual(x, True)
    
    def test_remove1(self):
        x = self.solution.remove(2)
        self.assertEqual(x, False)

if __name__ == '__main__':
    unittest.main()