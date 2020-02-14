import sqlite3


class MovieDB:
    __con = None
    __cur = None

    def __init__(self, name):
        name = name + ".db"

        self.__con = sqlite3.connect(name)
        self.__con.row_factory = sqlite3.Row
        self.__cur = self.__con.cursor()

    def my_create(self):
        self.__cur.execute("""                                 
            CREATE TABLE IF NOT EXISTS film (
                id INTEGER PRIMARY KEY ASC,
                title varchar(250) NOT NULL,
                genre varchar(250) DEFAULT '',
                time varchar(250) DEFAULT '',
                director varchar(250) DEFAULT '',
                country varchar(250) DEFAULT '',
                year varchar(250) DEFAULT ''
            )""")
        self.__con.commit()

    def my_menu(self):
        print("+----------------------------------+\n"
              "|           PANEL GŁÓWNY           |\n"
              "|----------------------------------|\n"
              "| 1 | Dodaj film                   |\n"
              "|---|------------------------------|\n"
              "| 2 | Edytuj film                  |\n"
              "|---|------------------------------|\n"
              "| 3 | Usuń film                    |\n"
              "|---|------------------------------|\n"
              "| 4 | Wyszukaj film                |\n"
              "|---|------------------------------|\n"
              "| 5 | Wyświetl wszystkie filmy     |\n"
              "|---|------------------------------|\n"
              "| 6 | Usuń wszystkie filmy         |\n"
              "|---|------------------------------|\n"
              "| 0 | Wyjdź                        |\n"
              "+----------------------------------+\n")

    def my_table(self, movies):
        print("+------------------------------------------------------------------------------+\n"
              "| ID |     Tytuł     |    Gatunek     | Czas |    Reżyser     |  Kraj   | Rok  |\n"
              "+------------------------------------------------------------------------------+")
        for movie in movies:
            id = self.my_fill(4, str(movie['id']))
            print("|"+str(id)+"|"+str(movie['title'])+"|"+str(movie['genre'])+"|"+str(movie['time'])+"|"
                  + str(movie['director'])+"|"+str(movie['country'])+"|"+str(movie['year'])+"|")
        print("+------------------------------------------------------------------------------+")

    def my_add(self):
        title = ""
        while title == "":
            print("+--------------------------------------------------------------+\n"
                  "| Podaj tytuł filmu [max 15 znaków] (wpisz 0 aby anulować)...  |\n"
                  "+--------------------------------------------------------------+")
            title = input()
            if title == "0":
                return

        while len(title) > 15:
            print("Zbyt duża ilość znaków! Spróbuj ponownie...")
            title = input()
            if title == "0":
                return
        titleshort = title
        title = self.my_fill(15, title)

        print("+--------------------------------------------------------------+\n"
              "| Podaj gatunek filmu [max 16 znaków]...                       |\n"
              "+--------------------------------------------------------------+")
        genre = input()
        while len(genre) > 16:
            print("Zbyt duża ilość znaków! Spróbuj ponownie...")
            genre = input()
        genre = self.my_fill(16, genre)

        print("+-------------------------------------------------------------+\n"
              "| Podaj czas trwania filmu w minutach [max 6 znaków]...       |\n"
              "+-------------------------------------------------------------+")
        time = input()
        while len(time) > 6:
            print("Zbyt duża ilość znaków! Spróbuj ponownie...")
            time = input()
        time = self.my_fill(6, time)

        print("+--------------------------------------------------------------+\n"
              "| Podaj reżysera filmu [max 15 znaków]...                      |\n"
              "+--------------------------------------------------------------+")
        director = input()
        while len(director) > 16:
            print("Zbyt duża ilość znaków! Spróbuj ponownie...")
            director = input()
        director = self.my_fill(16, director)

        print("+--------------------------------------------------------------+\n"
              "| Podaj kraj produkcji filmu [max 10 znaków]...                |\n"
              "+--------------------------------------------------------------+")
        country = input()
        while len(country) > 9:
            print("Zbyt duża ilość znaków! Spróbuj ponownie...")
            country = input()
        country = self.my_fill(9, country)

        print("+-------------------------------------------------------------+\n"
              "| Podaj rok produkcji filmu [max 6 znaków]...                 |\n"
              "+-------------------------------------------------------------+")
        year = input()
        while len(year) > 6:
            print("Zbyt duża ilość znaków! Spróbuj ponownie...")
            year = input()
        year = self.my_fill(6, year)

        self.__cur.execute('INSERT INTO film VALUES(NULL, ?, ?, ?, ?, ?, ?);', (title, genre, time, director, country, year))
        self.__con.commit()
        print("+----------------------------------------------+\n"
              '| Film "' + titleshort + '" został dodany do katalogu.\n'
              "+----------------------------------------------+")

    def my_fill(self, nr, string):
        if len(string) < nr:
            missing = nr - len(string)

            for i in range(missing):
                if i % 2 == 0:
                    string = string + " "
                if i % 2 == 1:
                    string = " " + string
        return string

    def my_edit(self):
        is_exit = self.my_search()
        if is_exit:
            return

        print("+--------------------------------------------------------------------+\n"
              "| Wybierz ID filmu, który chcesz edytować (wpisz 0 aby anulować)...  |\n"
              "+--------------------------------------------------------------------+")
        id = input()
        if id == "0":
            return

        self.__cur.execute("SELECT * FROM film WHERE id=?", (id,))
        movie = self.__cur.fetchone()

        if movie == None:
            print("Film o podanym ID nie istnieje!")
            return

        while 1:
            print("+----------------------------------+\n"
                  "|        Wybierz opcję:            |\n"
                  "|----------------------------------|\n"
                  "| 1 | Edytuj tytuł                 |\n"
                  "|---|------------------------------|\n"
                  "| 2 | Edytuj gatunek               |\n"
                  "|---|------------------------------|\n"
                  "| 3 | Edytuj czas trwania          |\n"
                  "|---|------------------------------|\n"
                  "| 4 | Edytuj reżysera              |\n"
                  "|---|------------------------------|\n"
                  "| 5 | Edytuj kraj produkcji        |\n"
                  "|---|------------------------------|\n"
                  "| 6 | Edytuj rok produkcji         |\n"
                  "|---|------------------------------|\n"
                  "| 0 | Powrót                       |\n"
                  "+----------------------------------+\n")
            choice = input()

            if choice == "0":
                break
            if choice == "1":
                title = ""
                exit = False
                while title == "":
                    print("+--------------------------------------------------------------+\n"
                          "| Podaj tytuł filmu [max 15 znaków] (wpisz 0 aby anulować)...  |\n"
                          "+--------------------------------------------------------------+")
                    title = input()
                    if title == "0":
                        exit = True
                        break

                while len(title) > 15:
                    print("Zbyt duża ilość znaków! Spróbuj ponownie...")
                    title = input()
                    if title == "0":
                        exit = True
                        break

                if not exit:
                    title = self.my_fill(15, title)
                    self.__cur.execute('UPDATE film SET title=? WHERE id=?', (title, id))
                    self.my_save(id)

            if choice == "2":
                print("+--------------------------------------------------------------+\n"
                      "| Podaj gatunek filmu [max 16 znaków]...                       |\n"
                      "+--------------------------------------------------------------+")
                genre = input()
                while len(genre) > 16:
                    print("Zbyt duża ilość znaków! Spróbuj ponownie...")
                    genre = input()
                genre = self.my_fill(16, genre)
                self.__cur.execute('UPDATE film SET genre=? WHERE id=?', (genre, id))
                self.my_save(id)

            if choice == "3":
                print("+-------------------------------------------------------------+\n"
                      "| Podaj czas trwania filmu w minutach [max 6 znaków]...       |\n"
                      "+-------------------------------------------------------------+")
                time = input()
                while len(time) > 6:
                    print("Zbyt duża ilość znaków! Spróbuj ponownie...")
                    time = input()
                time = self.my_fill(6, time)
                self.__cur.execute('UPDATE film SET time=? WHERE id=?', (time, id))
                self.my_save(id)

            if choice == "4":
                print("+--------------------------------------------------------------+\n"
                      "| Podaj reżysera filmu [max 15 znaków]...                      |\n"
                      "+--------------------------------------------------------------+")
                director = input()
                while len(director) > 16:
                    print("Zbyt duża ilość znaków! Spróbuj ponownie...")
                    director = input()
                director = self.my_fill(16, director)
                self.__cur.execute('UPDATE film SET director=? WHERE id=?', (director, id))
                self.my_save(id)

            if choice == "5":
                print("+--------------------------------------------------------------+\n"
                      "| Podaj kraj produkcji filmu [max 10 znaków]...                |\n"
                      "+--------------------------------------------------------------+")
                country = input()
                while len(country) > 9:
                    print("Zbyt duża ilość znaków! Spróbuj ponownie...")
                    country = input()
                country = self.my_fill(9, country)
                self.__cur.execute('UPDATE film SET country=? WHERE id=?', (country, id))
                self.my_save(id)

            if choice == "6":
                print("+-------------------------------------------------------------+\n"
                      "| Podaj rok produkcji filmu [max 6 znaków]...                 |\n"
                      "+-------------------------------------------------------------+")
                year = input()
                while len(year) > 6:
                    print("Zbyt duża ilość znaków! Spróbuj ponownie...")
                    year = input()
                year = self.my_fill(6, year)
                self.__cur.execute('UPDATE film SET year=? WHERE id=?', (year, id))
                self.my_save(id)

    def my_save(self, id):
        self.__con.commit()
        self.__cur.execute("SELECT * FROM film WHERE id=?", (id,))
        movie = self.__cur.fetchall()

        print("+----------------------------------------------+\n"
              "| Zmiany zostały zapisane:                     |\n"
              "+----------------------------------------------+")
        self.my_table(movie)

    def my_delete(self):
        is_exit = self.my_search()
        if is_exit:
            return

        print("+------------------------------------------------------------------+\n"
              "| Wybierz ID filmu, który chcesz usunąć (wpisz 0 aby anulować)...  |\n"
              "+------------------------------------------------------------------+")
        id = input()
        if id == "0":
            return

        self.__cur.execute("SELECT * FROM film WHERE id=?", (id,))
        movie = self.__cur.fetchone()

        if movie == None:
            print("Film o podanym ID nie istnieje!")
            return

        while 1:
            print("+----------------------------------------------+")
            print("Czy na pewno chesz usunąć:")
            self.__cur.execute("SELECT * FROM film WHERE id=?", (id,))
            movie = self.__cur.fetchall()
            self.my_table(movie)
            print("+----------------------------------+\n"
                  "|        Wybierz opcję:            |\n"
                  "|----------------------------------|\n"
                  "| 1 | Tak, usuń                    |\n"
                  "|---|------------------------------|\n"
                  "| 0 | Nie, nie usuwaj              |\n"
                  "+----------------------------------+")

            choice = input()

            if choice == "0":
                break
            if choice == "1":
                self.__cur.execute('DELETE FROM film WHERE id=?', (id,))
                self.__con.commit()
                print("+----------------------------------------------+\n"
                      "| Film został usunięty z katalogu              |\n"
                      "+----------------------------------------------+\n")
                break

    def my_search(self):
        while 1:
            print("+----------------------------------+\n"
                  "|        Wybierz opcję:            |\n"
                  "|----------------------------------|\n"
                  "| 1 | Wyświetl wszystkie filmy     |\n"
                  "|---|------------------------------|\n"
                  "| 2 | Wyszukiwanie po tytule       |\n"
                  "|---|------------------------------|\n"
                  "| 3 | Wyszukiwanie po gatunku      |\n"
                  "|---|------------------------------|\n"
                  "| 4 | Wyszukiwanie po reżyserze    |\n"
                  "|---|------------------------------|\n"
                  "| 0 | Powrót                       |\n"
                  "+----------------------------------+\n")
            choice = input()

            if choice == "0":
                return True
            if choice == "1":
                self.my_show()
                return False
            if choice == "2":
                movies = self.my_search_title()
                break
            if choice == "3":
                movies = self.my_search_genre()
                break
            if choice == "4":
                movies = self.my_search_director()
                break

        if movies == 0:
            return True
        else:
            self.my_table(movies)
        return False

    def my_search_title(self):
        print("+----------------------------------------------+\n"
              "| Podaj tytuł filmu...                         |\n"
              "+----------------------------------------------+")
        title = input()

        self.__cur.execute("SELECT COUNT(id) AS counter FROM film WHERE title LIKE '%" + title + "%';")
        number = self.__cur.fetchone()
        if self.is_empty(number['counter']):
            return 0
        else:
            self.__cur.execute("SELECT * FROM film WHERE title LIKE '%" + title + "%';")
            return self.__cur.fetchall()

    def my_search_genre(self):
        print("+----------------------------------------------+\n"
              "| Podaj gatunek filmu...                       |\n"
              "+----------------------------------------------+")
        genre = input()

        self.__cur.execute("SELECT COUNT(id) AS counter FROM film WHERE genre LIKE '%" + genre + "%';")
        number = self.__cur.fetchone()
        if self.is_empty(number['counter']):
            return 0
        else:
            self.__cur.execute("SELECT * FROM film WHERE genre LIKE '%" + genre + "%';")
            return self.__cur.fetchall()

    def my_search_director(self):
        print("+----------------------------------------------+\n"
              "| Podaj reżysera filmu...                      |\n"
              "+----------------------------------------------+")
        director = input()

        self.__cur.execute("SELECT COUNT(id) AS counter FROM film WHERE director LIKE '%" + director + "%';")
        number = self.__cur.fetchone()
        if self.is_empty(number['counter']):
            return 0
        else:
            self.__cur.execute("SELECT * FROM film WHERE director LIKE '%" + director + "%';")
            return self.__cur.fetchall()

    def is_empty(self, counter):
        if counter == 0:
            print("+----------------------------------------------+\n"
                  "| Brak filmów spełniających podane kryteria    |\n"
                  "+----------------------------------------------+")
            return True

    def my_show(self):
        self.__cur.execute("SELECT COUNT(id) AS counter FROM film;")
        number = self.__cur.fetchone()
        print("+----------------------------------------------+\n"
              "| Liczba wszystkich filmów: " + str(number['counter']) + "\n"
              "+----------------------------------------------+")

        self.__cur.execute("SELECT * FROM film;")
        movies = self.__cur.fetchall()
        self.my_table(movies)

    def my_drop(self):
        while 1:
            print("+----------------------------------------------+")
            print("| Czy na penwno chesz wyczyścić katalog?       |")
            print("+----------------------------------------------+")
            print("+----------------------------------+\n"
                  "|        Wybierz opcję:            |\n"
                  "|----------------------------------|\n"
                  "| 1 | Tak, wyczyść                 |\n"
                  "|---|------------------------------|\n"
                  "| 0 | Nie, nie czyść               |\n"
                  "+----------------------------------+\n")

            choice = input()

            if choice == "0":
                break
            if choice == "1":
                self.__cur.execute("DROP TABLE IF EXISTS film;")
                self.my_create()
                self.__con.commit()
                print("+----------------------------------+\n"
                      '| Katalog został wyczyszczony.     |\n'
                      "+----------------------------------+")
                break

    def my_exit(self):
        print("+------------------------------------------------------------------------------+\n"
              "|                                DO ZOBACZENIA                                 |\n"
              "+------------------------------------------------------------------------------+")
        exit()