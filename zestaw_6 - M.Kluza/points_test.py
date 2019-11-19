import unittest
from math import sqrt
from points import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(2, 4)
        self.p2 = Point(3, 6)
        self.p3 = Point(2, 4)

    def test_str(self):
        self.assertEqual(str(self.p1), "(2, 4)")
        self.assertEqual(str(self.p2), "(3, 6)")
        self.assertEqual(repr(self.p1), "Point(2, 4)")
        self.assertEqual(repr(self.p2), "Point(3, 6)")

    def test_eq(self):
        self.assertTrue(self.p1 == self.p3)
        self.assertTrue(self.p1 != self.p2)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(5, 10))
        self.assertEqual(self.p1 + self.p3, Point(4, 8))

    def test_sub(self):
        self.assertEqual(self.p2 - self.p1, Point(1, 2))
        self.assertEqual(self.p1 - self.p2, Point(-1, -2))
        self.assertEqual(self.p1 - self.p3, Point(0, 0))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 30)
        self.assertEqual(self.p1 * self.p3, 20)

    def test_cross(self):
        self.assertEqual(Point(2, 4).cross(Point(3, 6)), 0)
        self.assertEqual(Point(2, 4).cross(Point(4, 5)), -6)
        self.assertEqual(Point(-2, 4).cross(Point(-1, -1)), 6)

    def test_length(self):
        self.assertEqual(Point(2, 4).length(), sqrt(20))
        self.assertEqual(Point(4, 3).length(), 5)

    def tearDown(self):
        self.p1 = None
        self.p2 = None
        self.p3 = None


if __name__ == "__main__":
    unittest.main()  # wszystkie testy
