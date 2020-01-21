import random


def list_random_repeated(n):
    lista = list()
    for i in range(n):
        item = random.randint(0, n)
        lista.append(item)
    return lista


def mediana_sort(L, left, right):
    list_range = L[left:right+1]
    list_range_sorted = sorted(list_range)
    length = len(list_range_sorted)
    if length%2 == 0:
        median = (list_range_sorted[length//2] + list_range_sorted[(length//2)-1])/2
    else:
        median = list_range_sorted[length//2]

    print("W liscie L:", str(L), "w zakresie od", str(left), "do", str(right) + ",\nmediana wynosi: ", str(median) + ".")


L = list_random_repeated(10)
mediana_sort(L, 6, len(L)-1)
