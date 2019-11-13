#5.1 Stworzyć plik rekurencja.py i zapisać w nim funkcje z zadań 4.3 (factorial), 4.4 (fibonacci). Sprawdzić operacje importu i przeładowania modułu.

def factorial(n):
    """Iteracyjne obliczanie funkcji silnia n!"""
    x = 1
    for i in range(n):
        x = x * (i+1)
    return x


def fibonacci(n):
    """Ciąg Fibonacciego (definicja rekurencyjna)."""
    f1 = 0
    f2 = 1
    for i in range(n):
        f1, f2 = f2, f1 + f2
    return f1