import unittest
from prep import strange_function

class MyTestCase(unittest.TestCase):
    # def test_strange_function1(self):
    #     self.assertEqual(
    #         first=strange_function(1, 2, 3, 4),
    #         second='behaviour 3'
    #     )
        
    def test_behaviour1(self):
        self.assertEqual(
            first=strange_function(1, 1, 3, 4),
            second='behaviour 1'
    )
    
    def test_behaviour2(self):
        self.assertEqual(
            first=strange_function(1, 1, 4, 3),
            second='behaviour 2'
    )
    
    def test_behaviour3(self):
        self.assertEqual(
            first=strange_function(1, 2, 3, 4),
            second='behaviour 3'
    )
        
    def test_behaviour4(self):
        self.assertEqual(
            first=strange_function(3, 4, 1, 2),
            second='behaviour 4'
    )
        
    def test_behaviour5(self):
        self.assertEqual(
            first=strange_function(3, 2, 1, 4),
            second='behaviour 5'
    )
        
    def test_behaviour6(self):
        self.assertEqual(
            first=strange_function(1, 2, 1, 4),
            second='behaviour 6'
    )

# TODO: Can you write more test cases below to increase the test coverage of `strange_function`?