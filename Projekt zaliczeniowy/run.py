from my_functions import *


print("************************************************************************************\n"
      "*                                KATALOG FILMÓW                                    *\n"
      "************************************************************************************")

my_connect()
my_create()

while 1:
    my_menu()
    choice = input()

    if choice == "0":
        my_exit()
    if choice == "1":
        my_add()
    if choice == "2":
        my_edit()
    if choice == "3":
        my_delete()
    if choice == "4":
        my_search()
    if choice == "5":
        my_show()
    if choice == "6":
        my_drop()