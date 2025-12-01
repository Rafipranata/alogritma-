#pertemuan 11 - Perulangan Bersarang

#   Nama    = RAFI PRANATA
#   NPM     = 25670022 
#   KELAS   = 1A 

if __name__ == "__main__":
    #Array 
    #List
    #Inisialisasi List

    # list_angka = [8, 3 ,7 ,1 ,10, 12, 4]

    # print(list_angka[4])
    # list_angka[4] = 8
    # print(list_angka[4])

    # for i in list_angka:
    #     print(i, end=" ")
    #     print

    # i = 0
    # while (i < len(list_angka)):
    #     print(list_angka[i], end=" ")
    #     i += 1
    # print('')

    # data = ["bakso", "mi ayam", "seblak", "pecel"]

    # for idx, item in enumerate(data):
    #     print(f"index ke-{idx}: {item}")

    # print("Sebelum append")
    # for item in list_angka:
    #     print(item, end=" ")
    # print("")

    # list_angka.append(100)

    # print("Sesudah append")
    # for item in list_angka:
    #     print(item, end=" ")
    # print("")
    
    # print("Sebelum Insert")
    # for item in list_angka:
    #     print(item, end=" ")
    # print("")

    # list_angka.insert(0,100)

    # print("Sesudah Insert")
    # for item in list_angka:
    #     print(item, end=" ")
    # print("")

    # print("Sebelum Remove")
    # for item in list_angka:
    #     print(item, end=" ")
    # print("")

    # list_angka.remove(100)

    # print("Sesudah Remove")
    # for item in list_angka:
    #     print(item, end=" ")
    # print("")

    # print("Sebelum Delete")
    # for item in list_angka:
    #     print(item, end=" ")
    # print("")

    # # del list_angka(3)

    # print("Sesudah Delete")
    # for item in list_angka:
    #     print(item, end=" ")
    # print("")

    # data = ("bakso", "mi ayam", "seblak", "pecel")
    # for item in data:
    #     print(item, end=" ")
    # print("")


    # data_pelanggan = {
    #     "nama": "Rafi P",
    #     "tahun": "2025",
    #     "alamat": "Semarang"
    # }
    # print ("Nama Pelanggan")

    # for key in data_pelanggan:
    #     print(f"{key}: {data_pelanggan[key]}")

    
    matrikA = [
        [9, 2, 3],
        [3, 4, 5],
        [6, 7, 8],
    ]

    i = 0
    while(i < len(matrikA)):
        j=0
        while(j < len (matrikA[i])):
            print(matrikA[i][j], end=" ")
            j += 1
        i += 1 
        print("")

    data_karyawan = [
        {
            "nama": "Rafi P",
            "tahun": "2025",
            "alamat": "Semarang"
        },
        {
            "nama": "anonim, P",
            "tahun": "2025",
            "alamat": "Semarang"
        },
        {
            "nama": "anonim, P",
            "tahun": "2025",
            "alamat": "Semarang"
        },
    ]

    for idx, item in enumerate(data_karyawan):
        print("data karyawan ke-{idx}")
        for key in item:
            print(f"{key}: {item[key]}")
        print("")