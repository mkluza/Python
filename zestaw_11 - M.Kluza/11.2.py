from gen import *

def save(L, nr):
    file_name = "sort" + str(nr) + ".dat"
    file = open(file_name, "w")
    for i in range(len(L)):
        file.write(str(i) + "\t" + str(L[i]) + "\n")
    file.close()


def insert_sort(L, left, right):
    max_iter = (right-left)**2 // 4
    counter = 0
    flag = max_iter // 4
    save(L, 0)

    for i in range(left+1, right+1):
        item = L[i]
        j = i
        while j > left and L[j-1] > item:
            counter += 1
            if counter == flag:
                save(L, 1)
            if counter == 2 * flag:
                save(L, 2)
            if counter == 3 * flag:
                save(L, 3)
            L[j] = L[j-1]
            j = j-1
        L[j] = item

    save(L, 4)


L = list_random(100)
insert_sort(L, 0, len(L)-1)