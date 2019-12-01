import unittest
from triangles import Triangle
from points import Point

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.t1 = Triangle(2, 2, 4, 4, 6, 2)
        self.t2 = Triangle(4, 4, 2, 2, 6, 2)
        self.t3 = Triangle(1, 1, 3, 3, 5, 1)

    def test_str(self):
        self.assertEqual(str(self.t1), "[(2.0, 2.0), (4.0, 4.0), (6.0, 2.0)]")
        self.assertEqual(str(self.t2), "[(4.0, 4.0), (2.0, 2.0), (6.0, 2.0)]")
        self.assertEqual(str(self.t3), "[(1.0, 1.0), (3.0, 3.0), (5.0, 1.0)]")


    def test_repr(self):
        self.assertEqual(repr(self.t1), "Triangle(2.0, 2.0, 4.0, 4.0, 6.0, 2.0)")
        self.assertEqual(repr(self.t2), "Triangle(4.0, 4.0, 2.0, 2.0, 6.0, 2.0)")
        self.assertEqual(repr(self.t3), "Triangle(1.0, 1.0, 3.0, 3.0, 5.0, 1.0)")


    def test_eq(self):
        self.assertTrue(self.t1 == self.t2)
        self.assertTrue(self.t1 == self.t1)
        self.assertTrue(self.t1 != self.t3)

    def test_center(self):
        self.assertEqual(self.t1.center(), Point(4, 8/3))
        self.assertEqual(self.t2.center(), Point(4, 8/3))
        self.assertEqual(self.t3.center(), Point(3, 5/3))

    def test_area(self):
        self.assertEqual(self.t1.area(), 4)
        self.assertEqual(Triangle(0, 0, 0, 3, 6, 0).area(), 9)

    def test_move(self):
        self.assertEqual(self.t1.move(1, 1), Triangle(3, 3, 5, 5, 7, 3))
        self.assertEqual(self.t2.move(-1, 2), Triangle(3, 6, 1, 4, 5, 4))

    def test_make4(self):
        smaller = [Triangle(2, 2, 2+2, 2+2, 6, 2),
                   Triangle(2, 2, 2+4/3, 2+4/3, 6, 2),
                   Triangle(2, 2, 2+1, 2+1, 6, 2),
                   Triangle(2, 2, 2+4/6, 2+4/6, 6, 2)]
        self.assertEqual(Triangle(2, 2, 6, 6, 6, 2).make4(), smaller)

    def test_exception(self):
        ex1 = False
        ex2 = False
        try:
            Triangle(0, 0, 2, 2, 4, 4)
        except ValueError:
            ex1 = True
        try:
            Triangle(0, 0, "f", "a", 4, 3)
        except ValueError:
            ex2 = True
        self.assertTrue(ex1 and ex2)


    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()  #wszystkie testy


