import random

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    in_c = 0

    for i in range(n):
        x = random.random()
        y = random.random()

        if (x*x+y*y) <= 1:
            in_c += 1

    print("Liczba PI = " + str(4*in_c/n))