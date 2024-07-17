import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(self.calc.sub(3, 2), 1)
        self.assertEqual(self.calc.sub(2, 3), -1)
        self.assertEqual(self.calc.sub(2, 2), 0)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)
        self.assertEqual(self.calc.mul(5, 0), 0)
        self.assertEqual(self.calc.mul(-1, 2), -2)

    def test_div(self):
        self.assertEqual(self.calc.div(10, 2), 5)
        self.assertEqual(self.calc.div(5, 1), 5)
        self.assertEqual(self.calc.div(1, 2), 0.5)
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(10, 0)

    def test_pow(self):
        self.assertEqual(self.calc.pow(2, 3), 8)
        self.assertEqual(self.calc.pow(5, 0), 1)
        self.assertEqual(self.calc.pow(0, 5), 0)
        self.assertEqual(self.calc.pow(-2, 3), -8)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertEqual(self.calc.sqrt(0), 0)
        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)
