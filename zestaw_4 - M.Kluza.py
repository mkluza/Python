#################################
#          MARIUSZ KLUZA        #
#################################

#4.2 Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return.

def miarka(x):
    miarka = "|"
    skala = "0"

    for i in range(x):
        miarka += "....|"
        if i < 9:
            skala += ("    " + str(i + 1))
        else:
            skala += ("   " + str(i + 1))
    calosc = miarka + "\n" + skala
    return calosc

def prostokat(x, y):
    if int(x) == 0 or int(y) == 0:
        prostokat = ""
        return prostokat

    p = "+"
    q = "|"
    for i in range(int(y)):
        p += "---+"
        q += "   |"
    prostokat = p
    for i in range(int(x)):
        prostokat += "\n" + q + "\n" + p

    return prostokat

#4.3 Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def factorial(n):
    """Iteracyjne obliczanie funkcji silnia n!"""
    x = 1
    for i in range(n):
        x = x * (i+1)
    return x

assert factorial(5) == 120

#4.4 Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(n):
    """Ciąg Fibonacciego (definicja rekurencyjna)."""
    f1 = 0
    f2 = 1
    for i in range(n):
        f1, f2 = f2, f1 + f2
    return f1

assert fibonacci(5) == 5

#4.5 Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

def odwracanie_iter(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L

def odwracanie_rekur(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rekur(L, left+1, right-1)
    return L

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L1 = list(L)
assert odwracanie_iter(L, 3, 6) == [0, 1, 2, 6, 5, 4, 3, 7, 8, 9]
assert odwracanie_rekur(L1, 2, 5) == [0, 1, 5, 4, 3, 2, 6, 7, 8, 9]

#4.6 Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

def sum_seq(sequence):
    if len(sequence) == 0:
        return 0
    else:
        item = sequence[0]
        if isinstance(item, (list, tuple)):
            return sum_seq(item) + sum_seq(sequence[1:])
        else:
            return item + sum_seq(sequence[1:])

seq = [0, (1, [2, 3], 4, ()), 5, [[(6), 7], [8]], 9]
assert sum_seq(seq) == 45


#4.7 Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
# Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. Wskazówka: rozważyć wersję rekurencyjną,
# a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

def flatten(sequence):
    if len(sequence) == 0:
        return []
    else:
        item = sequence[0]
        if isinstance(item, (list, tuple)):
            return flatten(item) + flatten(sequence[1:])
        else:
            return [item] + flatten(sequence[1:])

seq = [0, (1, [2, 3], 4, ()), 5, [[(6), 7], [8]], 9]
assert flatten(seq) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]