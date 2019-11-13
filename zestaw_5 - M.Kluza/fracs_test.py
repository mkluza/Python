import unittest
from fracs import *

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-3, 9], [4, 6]), [1, 3])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([-3, -5], [10, 12]), [-7, 30])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([-3, 5], [2, -6]), [1, 5])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([3, -7], [1, 2]), [6, -7])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-2, 9]), False)
        self.assertEqual(is_positive([-7, -6]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([1, 2]), False)
        self.assertEqual(is_zero([0, 1]), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([0, 1], [0, 2]), 0)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([1, 1]), 1)
        self.assertEqual(frac2float([8, 2]), 4)

    def tearDown(self):
        self.zero = None

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy