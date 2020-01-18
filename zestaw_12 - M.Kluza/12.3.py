import random


def list_random_repeated(n):
    lista = list()
    for i in range(n):
        item = random.randint(0, n)
        lista.append(item)
    return lista


def mediana_sort(L, left, right):
    K = sorted(L)
    s = len(K)
    if s%2 == 0:
        m = (K[s//2] + K[(s//2)-1])/2
    else:
        m = K[s//2]

    print("W liscie L: " + str(L) + "\nmediana wynosi: " + str(m) + ".")


L = list_random_repeated(10)
mediana_sort(L, 0, len(L)-1)