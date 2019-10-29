#################################
#          MARIUSZ KLUZA        #
#################################

#3.1 Czy podany kod jest poprawny składniowo w Pythonie?
# 1) Tak, kod się kompiluje. W Pythnie zbędne jest jednak używanie ; na końcu linii oraz () po if.
# 2) Nie, kod się nie kompiluje. W Pythonie niezbędne jest przechodzenie do nowego wiersza
#   oraz używanie odpowiednich wcięć po pętlach i warunkach.
# 3) Nie, kod się nie kompiluje. Jest to wyrażenie trójargumentowe, brakuje jednak () przy funkcji print.

#3.2 Co jest złego w kodzie:
# 1) Metoda sort() niczego nie zwraca.
# 2) Przy pozycyjnym przypisywaniu krotki ilość elementów po lewej stronie znaku = musi być
#   taka samajak ilość elementów po prawej stronie znaku =.
# 3) Ten kod tworzy krotkę (tuplet). Krotki są niezmiennymi sekwencjami, jak łańcuchy.
#   Nie można ich modyfikować w miejscu i mają ustalony rozmiar.
# 4) Ten kod tworzy listę o rozmiarze 2 (liczonym od 0). Nie możemy dodać czegoś na miejsce,
#   które jest poza rozmiarem listy. Dopuszczalne jest natomiast dodawanie np. na koniec listy.
# 5) Łańcuchy znaków nie posiadają metody "append".
# 6) Funkcja pow() przyjmuje dwa argumenty (liczbę, którą podnosimy do potęgi i potęgę),
#   natomiast do funkcja map() można przekazać tylko funkcje przyjmujące jeden argment.


#3.3 Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.

for i in range(0, 31):
    if i%3!=0:
        print(i),

#3.4 Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący parę x i trzecią potęgę x.
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
# Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

while True:
    x = input("Podaj liczbe (aby zakonczyc wpisz 'stop'): ")
    try:
        print("x = " + str(float(x)) + "\t x^3 = " + str(float(x)**3))
    except ValueError:
        if x == 'stop':
            break
        print("BLAD! Wprowadz poprawna liczbe...")

#3.5 Napisać program rysujący "miarkę" o zadanej długości.
# Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
# Należy zbudować pełny string, a potem go wypisać.

print("Podaj długosc miarki:")
x = int(input())

miarka = "|"
skala = "0"

for i in range(x):
    miarka += "....|"
    if i < 9:
        skala += ("    " + str(i+1))
    else:
        skala += ("   " + str(i+1))
calosc = miarka + "\n" + skala
print(calosc)

#3.6 Napisać program rysujący prostokąt zbudowany z małych kratek.
# Należy zbudować pełny string, a potem go wypisać.

xy = input("Podaj wymiary prostokata (w formie AxB):")

x, y = xy.split("x")

if int(x) == 0 or int(y) == 0:
    quit()

p = "+"
q = "|"

for i in range(int(y)):
    p += "---+"
    q += "   |"

prostokat = p
for i in range(int(x)):
    prostokat += "\n" + q + "\n" + p

print(prostokat)

#3.8 Dla dwóch sekwencji znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

A = "pomidor"
B = "pomarancza"
list1 = []
list2 = []

for i in A:
    if i in B:
        if i not in list1:
            list1.append(i)

for i in A:
    if i not in list2:
        list2.append(i)
for i in B:
    if i not in list2:
        list2.append(i)

print(list1)
print(list2)

#3.9 Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
# Znaleźć listę zawierającą sumy liczb z tych sekwencji.
# Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].

A = [[],[4],(1,2),[3,4],(5,6,7)]
B = list()

for i in A:
    B.append(sum(i))

print(B)

#3.10 Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim
# (z literami I, V, X, L, C, D, M) na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

D1 = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
D2 = dict([("I",1), ("V",5), ("X",10), ("L",50), ("C",100), ("D",500), ("M",1000)])
D3 = dict(zip(["I", "V", "X", "L", "C", "D", "M"], [1, 5, 10, 50, 100, 500, 1000]))

def roman2int(x):
    wynik = 0
    skip = False
    for i in range(len(rom)):
        if skip:
            skip = False
            continue
        symbol1 = D1.get(rom[i])
        if i + 1 < len(rom):
            symbol2 = D1.get(rom[i + 1])
            if symbol1 >= symbol2:
                wynik += symbol1
            else:
                wynik += (symbol2 - symbol1)
                skip = True
        else:
            wynik += symbol1
    return wynik

while True:
    rom = input("Wprowadz rzymska liczbe (uzywaj jedynie I,V,X,L,C,D,M lub 'stop' by wyjsc):")
    if rom == 'stop':
        break
    print(roman2int(rom))