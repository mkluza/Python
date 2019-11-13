#5.2 Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach.
# Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik].
# Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions.
# Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.
from fractions import _gcd

def add_frac(frac1, frac2):
    numerator = frac1[0]*frac2[1] + frac2[0]*frac1[1]
    denumerator = frac1[1]*frac2[1]
    gcd = _gcd(numerator, denumerator)
    if abs(gcd) > 1:
        numerator /= gcd
        denumerator /= gcd

    return [int(numerator), int(denumerator)]

def sub_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    denumerator = frac1[1] * frac2[1]
    gcd = _gcd(numerator, denumerator)
    if abs(gcd) > 1:
        numerator /= gcd
        denumerator /= gcd

    return [int(numerator), int(denumerator)]

def mul_frac(frac1, frac2):
    numerator = frac1[0] * frac2[0]
    denumerator = frac1[1] * frac2[1]
    gcd = _gcd(numerator, denumerator)
    if abs(gcd) > 1:
        numerator /= gcd
        denumerator /= gcd

    return [int(numerator), int(denumerator)]

def div_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1]
    denumerator = frac1[1] * frac2[0]
    gcd = _gcd(numerator, denumerator)
    if abs(gcd) > 1:
        numerator /= gcd
        denumerator /= gcd

    return [int(numerator), int(denumerator)]

def is_positive(frac):
    return frac[0]/frac[1] >= 0

def is_zero(frac):
    return frac[0] == 0

def cmp_frac(frac1, frac2):
    f1 = frac2float(frac1)
    f2 = frac2float(frac2)
    if f1 > f2:
        return 1
    elif f1 < f2:
        return -1
    else:
        return 0

def frac2float(frac):
    return frac[0]/frac[1]