import datetime

matrix = {(0,0): 0.5, (0,1): 1, (1,0): 0}
def P(i,j):
    """Wersja dynamiczna"""
    global matrix
    if (i,j) in matrix.keys():
        return matrix.get((i,j))
    if i == 0:
        return matrix.get((0,1))
    if j == 0:
        return matrix.get((1,0))
    if i > 0 and j > 0:
        matrix[(i,j)] = 0.5 * (P(i-1,j) + P(i,j-1))
        return matrix.get((i,j))

def P_rek(i, j):
    """Wersja rekurencyjna"""
    if i == 0:
        if j == 0:
            return 0.5
        else:
            return 1
    else:
        if j == 0:
            return 0
        else:
            return 0.5 * (P_rek(i-1, j) + P_rek(i, j-1))


start = datetime.datetime.now()
P(11,11)
stop = datetime.datetime.now()
print("Czas dynamicznie: " + str((stop - start).microseconds))


start = datetime.datetime.now()
P_rek(11,11)
stop = datetime.datetime.now()
print("Czas rekurencyjnie: " + str((stop - start).microseconds))


for x in range(11):
    for y in range(11):
        assert P(x, y) == P_rek(x,y)