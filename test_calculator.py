# https://github.com/christyshao712/lab10-TB-CS.git
# Partner 1: Tanmay Bansal
# Partner 2: Christy Shao

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(-5, 7), 2)
        self.assertEqual(add(5.3, 1.1), 6.4)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(-2, -3), 1)
        self.assertEqual(sub(5, -3), 8)
        self.assertEqual(sub(5, 5), 0)

    ####### Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(1, 0), 0)
        self.assertEqual(mul(2, -10), -20)
        self.assertEqual(mul(14.1, 301.9), 4256.79)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(1, 1), 1)
        self.assertEqual(div(-2, -10), 5)
        self.assertEqual(div(4.6, 36.8), 8)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10, 10), 1)
        self.assertEqual(log(16, 2), 0.25)
        self.assertEqual(log(2, 16), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-1, 1)
    
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-10.1, -9.6), 13.934489585198303)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)


# Do not touch this
if __name__ == "__main__":
    unittest.main()