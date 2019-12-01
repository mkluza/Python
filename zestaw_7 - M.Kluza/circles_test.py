import unittest
from circles import Circle
from points import Point
from math import pi


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(0, 0, 2)
        self.c2 = Circle(1, 3, 2)

    def test_repr(self):
        self.assertEqual(repr(self.c1), "Circle(0.0, 0.0, 2.0)")
        self.assertEqual(repr(self.c2), "Circle(1.0, 3.0, 2.0)")


    def test_eq(self):
        self.assertTrue(self.c1 != self.c2)
        self.assertTrue(self.c1 == Circle(0, 0, 2))
        self.assertTrue(self.c1 != Circle(1, 0, 1))

    def test_area(self):
        self.assertEqual(self.c1.area(), pi*4)
        self.assertEqual(Circle(1, 3, 5).area(), pi*25)

    def test_move(self):
        self.assertEqual(self.c1.move(1, 1), Circle(1, 1, 2))
        self.assertEqual(self.c2.move(3, 2), Circle(4, 5, 2))

    def test_cover(self):
        self.assertEqual(Circle(0, 0, 2).cover(Circle(0, 0, 2)), Circle(0, 0, 2))
        self.assertEqual(Circle(0, 0, 2).cover(Circle(0, 0, 4)), Circle(0, 0, 4))
        self.assertEqual(Circle(0, 0, 2).cover(Circle(7, 0, 3)), Circle(3.5, 0, 6))
        self.assertEqual(Circle(1, 3, 3).cover(Circle(3, 3, 2)), Circle(2, 3, 3.5))

    def test_exception(self):
        ex1 = False
        ex2 = False
        try:
            Circle(2, "a", 2)
        except ValueError:
            ex1 = True
        try:
            Circle(1, 1, -2)
        except ValueError:
            ex2 = True
        self.assertTrue(ex1 and ex2)

    def tearDown(self): pass

if __name__ == "__main__":
        unittest.main()  # wszystkie testy

