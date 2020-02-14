from my_functions import *


def main():

    print("+------------------------------------------------------------------------------+\n"
          "|                                KATALOG FILMÓW                                |\n"
          "+------------------------------------------------------------------------------+")
    print("Podaj nazwę katalogu...")
    name = input()

    moviebase = MovieDB(name)

    moviebase.my_create()

    while 1:
        moviebase.my_menu()
        choice = input()

        if choice == "0":
            moviebase.my_exit()
        if choice == "1":
            moviebase.my_add()
        if choice == "2":
            moviebase.my_edit()
        if choice == "3":
            moviebase.my_delete()
        if choice == "4":
            moviebase.my_search()
        if choice == "5":
            moviebase.my_show()
        if choice == "6":
            moviebase.my_drop()


if __name__=="__main__":
    main()