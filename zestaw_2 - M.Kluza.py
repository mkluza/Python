
#################################
#          MARIUSZ KLUZA        #
#################################
#2.10 Mamy dany napis wielowierszowy line. Podaæ sposób obliczenia liczby wyrazów w napisie. Przez wyraz rozumiemy ci¹g "czarnych" znaków, oddzielony od innych wyrazów bia³ymi znakami (spacja, tabulacja, newline).
line = '''abd\tdef\ngh\nij'''
print(line)
print(len(line.split()))

#2.11 Podaæ sposób wyœwietlania napisu word tak, aby jego znaki by³y rozdzielone znakiem podkreœlenia.
print('_'.join('word'))

#2.12 Zbudowaæ napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudowaæ napis stworzony z ostatnich znaków wyrazów z wiersza line.
line = '''abd\tdef\tgh\tij'''

napis = line.split()
pierwsze = list()
ostatnie = list()
for i in range(0, len(napis)):
    pierwsze.append((napis[i])[0])
    ostatnie.append((napis[i])[len(napis[i])-1])

pierwsze = "".join(pierwsze)
ostatnie = "".join(ostatnie)
print(pierwsze)
print(ostatnie)

#2.13 ZnaleŸæ ³¹czn¹ d³ugoœæ wyrazów w napisie line. Wskazówka: mo¿na skorzystaæ z funkcji sum().
line = '''abd\tdef\tgh\tij'''

napis = line.split()
suma = list()
for i in range(0, len(napis)):
    suma.append(len(napis[i]))

wynik = sum(suma)
print(wynik)
#2.14 ZnaleŸæ: (a) najd³u¿szy wyraz, (b) d³ugoœæ najd³u¿szego wyrazu w napisie line.
line = '''abd\tdef\tghagh\tij'''

napis = line.split()
napis.sort(key=len)
napis.reverse()
print("Najdluzszy wyraz " '"'+ napis[0] +'"' " ma dlugosc " + str(len(napis[0])))

#2.15 Na liœcie L znajduj¹ siê liczby ca³kowite dodatnie. Stworzyæ napis bêd¹cy ci¹giem cyfr kolejnych liczb z listy L.
L = [3,53,4,75,2,111,37,4,89]

napis = list()
for i in range(0, len(L)):
    napis.append(str(L[i]))
napis = "".join(napis)
print(napis)

#2.16 W tekœcie znajduj¹cym siê w zmiennej line zamieniæ ci¹g znaków "GvR" na "Guido van Rossum".
line = "TEXT TEXT GvR TEXT GvR TEXT TEXT TEXT GvR TEXT"

napis = line.replace("GvR", "Guido van Rossum")
print(napis)
#2.17 Posortowaæ wyrazy z napisu line raz alfabetycznie, a raz pod wzglêdem d³ugoœci. Wskazówka: funkcja wbudowana sorted().
line = "pies kot chomik papuga delfin lis"

napis = line.split()
print("Alfabetycznie: " + str(sorted(napis, key=str.lower)))
print("Wedlug dlugosci: " + str(sorted(napis, key=len)))

#2.18 ZnaleŸæ liczbê cyfr zero w du¿ej liczbie ca³kowitej. Wskazówka: zamieniæ liczbê na napis.
x = 403424030200040000200123210000

napis = str(x)
n = 0
for i in napis:
    if i == "0":
        n+=1
print("Ilosc cyfr zero w liczbie " + napis + " to " + str(n))

#2.19 Na liœcie L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudowaæ napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe bêd¹ mia³y blok dope³niony zerami, np. 007, 024. Wskazówka: str.zfill().
L = [4,54,643,7,5,422,435,55,3,22,323,3]

napis = list()
for i in range(0, len(L)):
    a = (str(L[i])).zfill(3)
    napis.append(a)
print(napis)

input()