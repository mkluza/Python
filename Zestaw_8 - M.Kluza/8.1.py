def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0:
        if b == 0:
            if c == 0:
                print("Rownanie ma nieskonczona liczbe rozwiazan")
            else:
                print("Rownanie nie ma rozwiazan")
        else:
            if c == 0:
                print("Rozwiazanie rownania: y = 0")
            else:
                print("Rozwiazanie rownania: y = " + str(-c/b))
    else:
        if b == 0:
            if c == 0:
                print("Rozwiazanie rownania: x = 0")
            else:
                print("Rozwiazanie rownania: x = " + str(-c/a))
        else:
            if c == 0:
                print("Rozwiazanie rownania: y = " + str(-a/b) + "*x")
            else:
                print("Rozwiazanie rownania: y = " + str(-a/b) + "*x + " + str(-c/b))