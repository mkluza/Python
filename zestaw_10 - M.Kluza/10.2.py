class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise ValueError("Stos jest pelny.")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stos jest pusty.")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data

import unittest

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack_full = Stack(2)
        self.stack_empty = Stack(2)
        self.stack_full.push(1)
        self.stack_full.push(2)

    def test_exception(self):
        ex1 = False
        ex2 = False
        try:
            self.stack_full.push(3)
        except ValueError:
            ex1 = True
        try:
            self.stack_empty.pop()
        except ValueError:
            ex2 = True
        self.assertTrue(ex1 and ex2)


    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy

