import sqlite3

try:
    from texttable import Texttable
except ImportError:
    from pip._internal import main as pip
    pip(['install', 'texttable'])
    from texttable import Texttable


def my_connect():
    print("Podaj nazwę katalogu...")
    name = input()
    name = name + ".db"

    global con, cur
    con = sqlite3.connect(name)

    con.row_factory = sqlite3.Row

    cur = con.cursor()


def my_create():
    cur.execute("""                                 
        CREATE TABLE IF NOT EXISTS film (
            id INTEGER PRIMARY KEY ASC,
            title varchar(250) NOT NULL,
            genre varchar(250) DEFAULT '',
            time INTEGER DEFAULT NULL,
            director varchar(250) DEFAULT '',
            country varchar(250) DEFAULT '',
            year INTEGER DEFAULT NULL
        )""")
    con.commit()


def my_menu():
    print("____________________________________\n"
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
          "|__________________________________|\n")


def my_table(movies):
    t = Texttable()
    t.set_cols_width([3, 30, 20, 17, 15, 14, 13])
    t.set_cols_align(['c', 'c', 'c', 'c', 'c', 'c', 'c'])
    t.header(['ID', 'Tytuł', 'Gatunek', 'Czas trwania[min]', 'Reżyser', 'Kraj produkcji', 'Rok produkcji'])

    for movie in movies:
        t.add_row([movie['id'], movie['title'], movie['genre'], movie['time'], movie['director'], movie['country'],
              movie['year']])
    print(t.draw())


def my_add():
    title = ""
    while title == "":
        print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
              "+ Podaj tytuł filmu (wpisz 0 aby anulować)...  +\n"
              "++++++++++++++++++++++++++++++++++++++++++++++++")
        title = input()
        if title == "0":
            return

    print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
          "+ Podaj gatunek filmu...                       +\n"
          "++++++++++++++++++++++++++++++++++++++++++++++++")
    genre = input()

    print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
          "+ Podaj czas trwania filmu w minutach...       +\n"
          "++++++++++++++++++++++++++++++++++++++++++++++++")
    time = input()

    print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
          "+ Podaj reżysera filmu...                      +\n"
          "++++++++++++++++++++++++++++++++++++++++++++++++")
    director = input()

    print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
          "+ Podaj kraj produkcji filmu...                +\n"
          "++++++++++++++++++++++++++++++++++++++++++++++++")
    country = input()

    print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
          "+ Podaj rok produkcji filmu...                 +\n"
          "++++++++++++++++++++++++++++++++++++++++++++++++")
    year = input()

    cur.execute('INSERT INTO film VALUES(NULL, ?, ?, ?, ?, ?, ?);', (title, genre, time, director, country, year))
    con.commit()
    print("=====================================================\n"
          ' Film "' + title + '" został dodany do katalogu.\n'
          "=====================================================")


def my_edit():
    is_exit = my_search()
    if is_exit:
        return

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
          "+ Wybierz ID filmu, który chcesz edytować (wpisz 0 aby anulować)...  +\n"
          "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    id = input()
    if id == "0":
        return

    cur.execute("SELECT * FROM film WHERE id=?", (id,))
    movie = cur.fetchone()

    if movie == None:
        print("Film o podanym ID nie istnieje!")
        return

    while 1:
        print("____________________________________\n"
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
              "|__________________________________|\n")
        choice = input()

        if choice == "0":
            break
        if choice == "1":
            title = ""
            while title == "":
                print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
                      "+ Podaj tytuł filmu (wpisz 0 aby anulować)...  +\n"
                      "++++++++++++++++++++++++++++++++++++++++++++++++")
                title = input()
                if title == "0":
                    break
            cur.execute('UPDATE film SET title=? WHERE id=?', (title, id))
            my_save(id)

        if choice == "2":
            print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
                  "+ Podaj gatunek filmu...                       +\n"
                  "++++++++++++++++++++++++++++++++++++++++++++++++")
            genre = input()
            cur.execute('UPDATE film SET genre=? WHERE id=?', (genre, id))
            my_save(id)

        if choice == "3":
            print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
                  "+ Podaj czas trwania filmu w minutach...       +\n"
                  "++++++++++++++++++++++++++++++++++++++++++++++++")
            time = input()
            cur.execute('UPDATE film SET time=? WHERE id=?', (time, id))
            my_save(id)

        if choice == "4":
            print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
                  "+ Podaj reżysera filmu...                      +\n"
                  "++++++++++++++++++++++++++++++++++++++++++++++++")
            director = input()
            cur.execute('UPDATE film SET director=? WHERE id=?', (director, id))
            my_save(id)

        if choice == "5":
            print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
                  "+ Podaj kraj produkcji filmu...                +\n"
                  "++++++++++++++++++++++++++++++++++++++++++++++++")
            country = input()
            cur.execute('UPDATE film SET country=? WHERE id=?', (country, id))
            my_save(id)

        if choice == "6":
            print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
                  "+ Podaj rok produkcji filmu...                 +\n"
                  "++++++++++++++++++++++++++++++++++++++++++++++++")
            year = input()
            cur.execute('UPDATE film SET year=? WHERE id=?', (year, id))
            my_save(id)


def my_save(id):
    con.commit()
    cur.execute("SELECT * FROM film WHERE id=?", (id,))
    movie = cur.fetchall()

    print("=====================================================\n"
          " Zmiany zostały zapisane:\n"
          "=====================================================")
    my_table(movie)


def my_delete():
    is_exit = my_search()
    if is_exit:
        return

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
          "+ Wybierz ID filmu, który chcesz usunąć (wpisz 0 aby anulować)...  +\n"
          "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    id = input()
    if id == "0":
        return

    cur.execute("SELECT * FROM film WHERE id=?", (id,))
    movie = cur.fetchone()

    if movie == None:
        print("Film o podanym ID nie istnieje!")
        return

    while 1:
        print("=====================================================")
        print("Czy na pewno chesz usunąć:")
        cur.execute("SELECT * FROM film WHERE id=?", (id,))
        movie = cur.fetchall()
        my_table(movie)
        print("____________________________________\n"
              "|        Wybierz opcję:            |\n"
              "|----------------------------------|\n"
              "| 1 | Tak, usuń                    |\n"
              "|---|------------------------------|\n"
              "| 0 | Nie, nie usuwaj              |\n"
              "|__________________________________|\n")

        choice = input()

        if choice == "0":
            break
        if choice == "1":
            cur.execute('DELETE FROM film WHERE id=?', (id,))
            con.commit()
            print("=====================================================\n"
                  " Film został usunięty z katalogu \n"
                  "=====================================================\n")
            break


def my_search():
    while 1:
        print("____________________________________\n"
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
              "|__________________________________|\n")
        choice = input()

        if choice == "0":
            return True
        if choice == "1":
            my_show()
            return False
        if choice == "2":
            movies = my_search_title()
            break
        if choice == "3":
            movies = my_search_genre()
            break
        if choice == "4":
            movies = my_search_director()
            break

    if movies == 0:
        return True
    else:
        my_table(movies)
    return False


def my_search_title():
    print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
          "+ Podaj tytuł filmu...                         +\n"
          "++++++++++++++++++++++++++++++++++++++++++++++++")
    title = input()

    cur.execute("SELECT COUNT(id) AS counter FROM film WHERE title LIKE '%" + title + "%';")
    number = cur.fetchone()
    if is_empty(number['counter']):
        return 0
    else:
        cur.execute("SELECT * FROM film WHERE title LIKE '%" + title + "%';")
        return cur.fetchall()


def my_search_genre():
    print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
          "+ Podaj gatunek filmu...                       +\n"
          "++++++++++++++++++++++++++++++++++++++++++++++++")
    genre = input()

    cur.execute("SELECT COUNT(id) AS counter FROM film WHERE genre LIKE '%" + genre + "%';")
    number = cur.fetchone()
    if is_empty(number['counter']):
        return 0
    else:
        cur.execute("SELECT * FROM film WHERE genre LIKE '%" + genre + "%';")
        return cur.fetchall()


def my_search_director():
    print("++++++++++++++++++++++++++++++++++++++++++++++++\n"
          "+ Podaj reżysera filmu...                      +\n"
          "++++++++++++++++++++++++++++++++++++++++++++++++")
    director = input()

    cur.execute("SELECT COUNT(id) AS counter FROM film WHERE director LIKE '%" + director + "%';")
    number = cur.fetchone()
    if is_empty(number['counter']):
        return 0
    else:
        cur.execute("SELECT * FROM film WHERE director LIKE '%" + director + "%';")
        return cur.fetchall()


def is_empty(counter):
    if counter == 0:
        print("=====================================================\n"
              " Brak filmów spełniających podane kryteria           \n"
              "=====================================================")
        return True


def my_show():
    cur.execute("SELECT COUNT(id) AS counter FROM film;")
    number = cur.fetchone()
    print("=====================================================\n"
          " Liczba wszystkich filmów: " + str(number['counter']) + "\n"
          "=====================================================")

    cur.execute("SELECT * FROM film;")
    movies = cur.fetchall()

    my_table(movies)


def my_drop():
    while 1:
        print("=====================================================")
        print(" Czy na penwno chesz wyczyścić katalog?")
        print("=====================================================")
        print("____________________________________\n"
              "|        Wybierz opcję:            |\n"
              "|----------------------------------|\n"
              "| 1 | Tak, wyczyść                 |\n"
              "|---|------------------------------|\n"
              "| 0 | Nie, nie czyść               |\n"
              "|__________________________________|\n")

        choice = input()

        if choice == "0":
            break
        if choice == "1":
            cur.execute("DROP TABLE IF EXISTS film;")
            my_create()
            con.commit()
            print("=====================================================\n"
                  ' Katalog został wyczyszczony.\n'
                  "=====================================================")
            break


def my_exit():
    print("************************************************************************************\n"
          "*                                DO ZOBACZENIA                                     *\n"
          "************************************************************************************")
    from pip._internal import main as pip
    pip(['uninstall', 'texttable'])
    exit()