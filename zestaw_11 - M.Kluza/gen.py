import random

def list_random(n):
    lista = list(range(n))
    random.shuffle(lista)
    return lista

def list_almost_sorted(n):
    lista = list(range(n))
    for i in range(0, n-1, 2):
        lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista

def list_almost_sorted_r(n):
    lista = list_almost_sorted(n)
    lista.reverse()
    return lista

def list_random_gauss(n):
    lista = list()
    for i in range(n):
        item = random.gauss(0, 1)
        lista.append(item)
    return lista

def list_random_repeated(n, k):
    if k > n:
        raise ValueError("Liczba k musi być mniejsza on n")
    lista = list()
    for i in range(n):
        item = random.randint(0, k-1)
        lista.append(item)
    return lista



