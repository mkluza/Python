from random import randint

class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def create_bst(size):
    root = None
    for i in range(size):
        data = randint(-20, 20)
        node = Node(data)
        root = bst_insert(root, node)

    return root

def bst_insert(root, node):   # zwraca nowy korzeń
    if root is None:
        return node
    if node.data < root.data:
        root.left = bst_insert(root.left, node)
    elif node.data > root.data:
        root.right = bst_insert(root.right, node)
    else:
        pass          # ignorujemy duplikaty
    return root            # bez zmian


def print_inorder(root):
    if root is None:
        return
    print_inorder(root.left)
    print(root, end=", ")
    print_inorder(root.right)

def bst_max(root):
    if root is None:
        raise ValueError("Drzewo jest puste.")
    max = root
    while max.right:
        max = max.right

    return max


def bst_min(root):
    if root is None:
        raise ValueError("Drzewo jest puste.")
    min = root
    while min.left:
        min = min.left

    return min