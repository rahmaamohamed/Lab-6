import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        # Test addition functionality
        result = Calculator.add(3, 7)
        self.assertEqual(result, 10)
        
        result = Calculator.add(-1, 1)
        self.assertEqual(result, 0)
        
        result = Calculator.add(-1, -1)
        self.assertEqual(result, -2)

    def test_subtract(self):
        # Test subtraction functionality
        result = Calculator.subtract(10, 5)
        self.assertEqual(result, 5)
        
        result = Calculator.subtract(-1, -1)
        self.assertEqual(result, 0)

    def test_multiply(self):
        # Test multiplication functionality
        result = Calculator.multiply(3, 7)
        self.assertEqual(result, 21)
        
        result = Calculator.multiply(-1, 1)
        self.assertEqual(result, -1)

    def test_divide(self):
        # Test division functionality
        result = Calculator.divide(10, 2)
        self.assertEqual(result, 5)
        
        result = Calculator.divide(-6, 3)
        self.assertEqual(result, -2)

        # Test division by zero, expecting a ValueError
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
