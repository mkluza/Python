import random


def random_linear_search(n, k):
    if k > n:
        raise ValueError("Liczba k musi być mniejsza on n")
    L = list()
    for i in range(n):
        item = random.randint(0, k-1)
        L.append(item)

    y = random.randint(0, k-1)
    Y = ""

    j = 0
    counter = 0
    while j < n:
        if L[j] == y:
            if counter == 0:
                Y += str(j)
            else:
                Y += ", " + str(j)
            counter += 1
        j += 1
    Y += "."

    print("W liscie L: " + str(L) + "\nliczba '" + str(y) + "' wystepuje " + str(counter) + " razy, na pozycjach nr: " + Y)


random_linear_search(100, 10)