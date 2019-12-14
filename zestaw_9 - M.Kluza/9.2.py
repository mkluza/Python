from random import randint

class SingleList:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def search(self, data):
        # Zwraca łącze do węzła o podanym kluczu lub None.
        if self is None:
            raise ValueError("Lista jest pusta.")

        while self:
            if self.data == data:
                return self  # zwracamy węzeł z danymi
            self = self.next
        return None

    def reverse(self):  # zwraca nowy head
        # Zwraca łącze do węzła z najmniejszym kluczem.
        if self is None:
            raise ValueError("Lista jest pusta.")

        before = None
        after = self
        while after:
            node = after.next
            after.next = before
            before = after
            after = node
        return before

    def find_max(self):
        # Zwraca łącze do węzła z największym kluczem.
        if self is None:
            raise ValueError("Lista jest pusta.")

        max = self
        while self:
            if self.data > max.data:
                max = self
            self = self.next

        return max

    def find_min(self):
        # Zwraca łącze do węzła z najmniejszym kluczem.
        if self is None:
            raise ValueError("Lista jest pusta.")

        min = self
        while self:
            if self.data < min.data:
                min = self
            self = self.next

        return min



def create_list(size):
    head = None

    for i in range(size):
        data = randint(-20, 20)
        head = SingleList(data, head)

    return head

def print_list(node):
    """Iteracyjne wypisanie listy jednokierunkowej."""
    while node:
        print(node, end=", ")
        node = node.next