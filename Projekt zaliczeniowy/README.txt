Projekt zaliczeniowy: Katalog filmów			
Autor: Mariusz Kluza			
Data: 10.02.2020			

######################################### 
Informacje ogólne:

Projekt realizuje implementacjê katalogu filmów z wykorzystaniem jêzyka Python3 i baz danych SQLite. 

######################################### 
Uruchamianie:

Aby uruchomiæ program nale¿y u¿yæ komendy:
>>> python run.py

Podczas uruchomienia program automatycznie (przy u¿yciu pip) instaluje bibliotekê niezbêdn¹ do poprawnego wyœwietlania danych. Biblioteka ta mo¿e zostaæ automatycznie odinstalowana podczas zamykania programu, wedle ¿yczenia u¿ytkownika.

######################################### 
Zawartoœæ:

README.txt 
Plik tekstowy zawieraj¹cy dokumentacjê.

run.py
Plik uruchamiaj¹cy aplikacje, zawieraj¹cy g³ówn¹ pêtle programu.

my_functions.py
Plik zawieraj¹cy wszystkie funkcje u¿yte w programie.

movies.db
Przyk³adowa baza danych.

######################################### 
Metody:

my_connect()
Metoda najpierw pyta o nazwê bazy danych (bez rozszerzenia!), z któr¹ chcemy siê po³¹czyæ (jeœli baza o podanej nazwie nie istnieje, tworzona jest automatycznie nowa baza). Nastêpnie tworzy po³¹czenie z baz¹ oraz tworzy obiekt kursora niezbêdny do wykonywania opercaji na bazie.


my_create()
Metoda tworzy tabelê o ustalonych odgórnie kolumnach i zapisuje j¹ do bazy.


my_menu()
Metoda wyœwietlaj¹ca opcjê panelu g³ównego aplikacji.


my_table()
Metoda pobiera jako argument listê rekordów. U¿ywaj¹c biblioteki 'texttable' (s³u¿¹cej do wizulanej prezentacji danych) tworzy tabelê o odpowiednich nag³ówkach, a nastêpnie przechodz¹c po kolejnych rekordach listy, dodaje dane do tabeli, któr¹ na koniec wyœwietla.


my_add()
Metoda s³u¿y do dodania nowej pozycji do bazy danych. Kolejno pyta o: tytu³ (niezbêdny), gatunek, czas trwania, re¿ysera, kraj produkcji oraz rok produkcji. Nasêtêpnie dodaje wpisane dane do bazy, zapisuje i wyœwietla odpowiedni komunikat.


my_edit()
Metoda s³u¿y do edycji istniej¹cych pozycji w bazie. Na pocz¹tku wywo³uje metodê my_show(), aby pokazaæ istniej¹ce w bazie filmy. Nastepnie pyta o ID filmu, który chcemy edytowaæ (jeœli ID nie istnieje to wyœwietla odpowiedni komunikat). Po wybraniu odpowiedniego ID wyœwietla listê opcji jakich mo¿emy u¿yæ do edycji filmu. Po wybraniu i zatwierdzeniu zmiany wywo³uje metode my_save. W metodzie zawarta jest nieskoñczona pêtla, któr¹ opuœciæ mo¿na wybieraj¹c odpowiedni¹ opcjê ("Powrót").


my_save()
Metoda jako argument przyjmuje ID filmu który zosta³ edytowany. Zapisuje dane zmiany do bazy i wyœwietla odpowiedni komunikat.


my_delete()
Metoda s³u¿y do usuniêcia istniej¹cej pozycji z bazy. Na pocz¹tku wywo³uje metodê my_show(), aby pokazaæ istniej¹ce w bazie filmy. Nastepnie pyta o ID filmu, który chcemy usun¹æ (jeœli ID nie istnieje to wyœwietla odpowiedni komunikat). Po wybraniu odpowiedniego ID wyœwietla komunikat pytaj¹cy o potwierdzenie naszej decyzji. Zale¿nie od wyboru albo pozostawia film w bazie i wraca do panelu g³ównego, albo usuwa rekord z bazy, zapisuje zmiany i wyœwietla odpowiedni komunikat.


my_search()
Funkcja filtruje i wyœwietla filmy zapisane w bazie. Mo¿e wyœwietliæ wszystkie rekordy (my_show()) lub odpowiednio je przefiltrowaæ po: tytule, gatunku czy re¿yserze. Trzy ostatnie opcje przekierowuj¹ nas do odpowiednich fukcji pomocniczych. Na koniec przekazuje otrzymane rekordy do metody my_table.


my_search_title(), my_search_genre(), my_search_director()
Funkcje nak³adj¹ odpowiednie filtry. Wywo³uj¹ fukjê is_empty i zwracaj¹ odpowiednie wyniki. 


is_empty()
Funkcja sprawdza czy istnieje chocia¿ jeden rekord spe³niaj¹cy na³o¿one warunki, wyœwietla odpowiedni komunikat i zwraca odpowiedni¹ wartoœæ logiczn¹.


my_show()
Metoda wyœwietla wszystkie filmy znajduj¹ce siê w bazie. Wyœwitla iloœæ wszystkich zapisanych rekordów, a na koniec przekazuje otrzymane rekordy do metody my_table.


my_drop()
Metoda s³u¿y do usuwania wszystkich rekordów z bazy czyli do czyszczenia ca³ego katalogu. Wyœwietla komunikat pytaj¹cy o potwierdzenie naszej decyzji. Zale¿nie od wyboru albo wraca do panelu g³ównego, albo usuwa ca³¹ tablice z bazy i wywo³uje metodê my_create(). Nastepnie zapisuje zmiany i wyœwietla odpowiedni komunikat.


my_exit()
Metoda zamykaj¹ca program. Wyœwietla komunikat ¿egnaj¹cy i koñczy dzia³anie programu.