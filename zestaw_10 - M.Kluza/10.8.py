from random import randint


class RandomQueue:

    def __init__(self, size=5):
        self.max_size = size
        self.size = 0
        self.items = self.max_size * [None]

    def __str__(self):          # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def insert(self, item):
        if self.is_full():
            raise ValueError("Kolejka jest pelna.")
        self.items[self.size] = item
        self.size += 1

    def remove(self):    # zwraca losowy element
        if self.is_empty():
            raise ValueError("Kolejka jest pusta.")
        index = randint(0, self.size-1)
        item = self.items[index]
        self.items[index] = self.items[self.size-1]
        self.items[self.size - 1] = None
        self.size -= 1
        return item


    def clear(self):     # czyszczenie listy
        while not self.is_empty():
            self.remove()