#pertemuan 13 - Sorting

#   Nama    = RAFI PRANATA
#   NPM     = 25670022 
#   KELAS   = 1A 
import sorting 

if __name__ == "__main__":
    #Cara menukar 2 variable
    angka1 = 20
    angka2 = 8
    angka3 = [1,2,3]
    x = sum(angka3)

    print("Sebelum Swap")
    print(angka1)
    print(angka2)
    print(angka3)
    print(x)

    print("Sesudah Swap")

    temp = angka1
    angka1 = angka2
    angka2 = temp

    print("Sebelum Swap")
    print(angka1)
    print(angka2)

    list_angka = [9,8,5,3,2,1]

    print("Sebelum Bubble Sort")
    sorting.cetak_list(list_angka)

    sorting.bubble_sort_asc(list_angka)
    print("Sesudah Bubble Sort")
    sorting.cetak_list(list_angka)


    list_angka = [21 ,25 ,38 ,1 ,2 ,4 ,5,]

    print("Sebelum Bubble Sort")
    sorting.cetak_list(list_angka)

    sorting.bubble_sort_desc(list_angka)
    print("Sesudah Bubble Sort")
    sorting.cetak_list(list_angka)