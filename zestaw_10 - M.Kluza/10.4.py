class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise ValueError("Kolejka jest pelna.")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise ValueError("Kolejka jest pusta.")
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data

import unittest

class TestStack(unittest.TestCase):

    def setUp(self):
        self.queue_full = Queue(2)
        self.queue_empty = Queue(2)
        self.queue_full.put(1)
        self.queue_full.put(2)

    def test_exception(self):
        ex1 = False
        ex2 = False
        try:
            self.queue_full.put(3)
        except ValueError:
            ex1 = True
        try:
            self.queue_empty.get()
        except ValueError:
            ex2 = True
        self.assertTrue(ex1 and ex2)


    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy

