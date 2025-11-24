#pertemuan 9 - Perulangan Bersarang

#   Nama    = RAFI PRANATA
#   NPM     = 25670022 
#   KELAS   = 1A 

if __name__ == "__main__":
    
    # for i in range(1, 6):
    #     print(f"Outer Loop ke-{i}")
    #     for j in range(1,4):
    #         print(f"Inner Loop ke-{j}")
    #     print("=======================")


    # a = 1
    # while(a <= 5):
    #     print(f"loop  outer loop a ke-{a}")
    #     i = 1
    #     while(i <= 3):
    #         print(f"loop i ke-{i}")
    #         i += 1
    #     a += 1
    #     print("=======================")

    # print("Bintang Pola Persegi")
    # batas = int(input("Masukan Batas Pola: "))

    # for x in range(0,batas):
    #     y = 1
    #     while(y <= batas):
    #         print(f"{y}", end="")
    #         y += 1
    #     print("")

    # print("=================")
    # x = 0
    # while(x <= batas + 1):
    #     for i in range(x):
    #         print(f"{i}", end="")
    #     x += 1
    #     print("")
    # x = 0
    # while(x <= batas):
    #     for i in range(batas - x):
    #         print(f"{i}", end="")
    #     x += 1
    #     print("")

    name = "Admin"
    pw = "12345678"

    batas_login = 0
    while(batas_login <= 5):

        login_user = input("Masukan UserName Anda: ")
        login_password = input("Masukan Password Anda: ")

        if(login_user == name and login_password == pw):
            batas_login = 5

            pilih = 0

            while(pilih != 5):
                print("Berhasil ✅")
                print("-----------Selamat datang di M-banking Berdiri----------------")
                print("1. Cek Saldo ")
                print("2. Transfer")
                print("3. Top Up")
                print("4. Poin dan Promo")
                print("5. Keluar")
                pilih = int(input("Masukan pilihan anda: "))

                if(pilih == 1):
                    print("Cek Saldo")
                elif(pilih == 2):
                    print("Transfer")
                elif(pilih == 3):
                    print("Top Up")
                elif(pilih == 4):
                    print("Poin dan Promo")
                elif(pilih == 5):
                    print("Terimakasi telah pakai bank berdiri")

        else:
            batas_login+=1
            print("Username dan Password yang adna masukan salah")
            print(f"Coba Lagi. Kesempatan {5-batas_login} Kali lagi")
            

