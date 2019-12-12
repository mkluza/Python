from math import sqrt

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Podane liczby nie spelniaja warunku trojkata")

    if a+b <= c or b+c <= a or c+a <= b:
        raise ValueError("Podane liczby nie spelniaja warunku trojkata")

    p = (a+b+c)/2
    S = sqrt(p * (p-a) * (p-b) * (p-c))

    print("Pole trojkat wynosi: " + str(S))