import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, 7), 12)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(8, 4), 4)
        self.assertEqual(self.calc.subtract(2, 1), 1)

        def __neg__(self) -> int:
            return self.assertEqual(self.calc.subtract(-3, -1), -4)


    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 3), 9)
        self.assertEqual(self.calc.multiply(-7, 2), -14)
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(-12, 3), -4)
        self.assertEqual(self.calc.divide(3, 0), None)



if __name__ == "__main__":
    unittest.main()