#pertemuan 9 - Analisa Perulangan

#   Nama    = RAFI PRANATA
#   NPM     = 25670022 
#   KELAS   = 1A 

if __name__ == "__main__":
    #Perulangan For
    # print("Perulangan For")
    # for i in range(1, 11):
    #     print("Angka", i)

    # print("Perulangan While")
    # x = 1 #Nilai awal
    # while(x <= 10): #Batasan
    #     print("Angka", x)
    #     x +=1 # Iterasi

    # print("Perulangan While")
    # a = 10 #Nilai awal
    # while(a >= 1): #Batasan
    #     print("Angka", a)
    #     a -=1 # Iterasi

    # pilihan = 1 #Nilai awal
    # while(pilihan > 0): #Batasan
    #     pilihan = int(input("Masukan Pilhan Anda: "))
    #     if(pilihan == 5):
    #         break
    #     print("Anda Memilih Angka", pilihan)
    
    # #Penggunaan Continue
    # for x in range(1, 11):
    #     if x % 3 == 0:
    #         continue
    #     print("Angka", x)

    # for x in range(1, 101):
    #     if x % 2 != 0:
    #         print(x, end="")
    # print("")

    pilihan = 1 
    while(pilihan <= 100): #Batasan
        if(pilihan % 2 == 0):
            print(pilihan, end=" ")
        pilihan +=1
    print("")
            