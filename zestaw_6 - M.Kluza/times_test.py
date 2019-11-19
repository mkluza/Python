import unittest
from times import Time

class TestTime(unittest.TestCase):

    def setUp(self):
        self.t1 = Time(1)
        self.t2 = Time(2)
        self.t3 = Time(3)
        self.t3601 = Time(3601)

    def test_print(self):       # test str() i repr()
        self.assertEqual(str(self.t1), "00:00:01")
        self.assertEqual(str(self.t3601), "01:00:01")
        self.assertEqual(repr(self.t1), "Time(1)")
        self.assertEqual(repr(self.t3601), "Time(3601)")


    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(self.t1 + self.t2, self.t3)

    def test_cmp(self):
        # Można sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Time(1) == Time(1))
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(3) > Time(2))
        self.assertTrue(self.t2 >= self.t1)
        self.assertTrue(self.t2 < self.t3601)
        self.assertTrue(self.t2 <= self.t2)


    def test_int(self):
        self.assertEqual(int(Time(1)), 1)
        self.assertEqual(int(self.t2), 2)
        self.assertEqual(int(Time(123)), 123)
        self.assertEqual(int(self.t3601), 3601)


    def tearDown(self):
        self.t1 = None
        self.t2 = None
        self.t3 = None
        self.t3601 = None

if __name__ == "__main__":
    unittest.main()     # wszystkie testy

