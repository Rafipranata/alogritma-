#pertemuan 5 - quiz

#   Nama    = RAFI PRANATA
#   NPM     = 25670022 
#   KELAS   = 1A 

if __name__ == "__main__":
    
    # buah = "apel"

    # nama = input("masukan nama: ")
    # password = input("masukan password: ")

    # if (nama == "Rafi" and password == "rafi"):
    #     print("Login Berhasil")
    # else:
    #     print("Login Gagal")
    belanja = float(input("Masukan Total belanja: "))

    if(belanja > 500000):
        diskon = 0.2
    elif(belanja > 200000):
        diskon = 0.1
    elif(belanja > 100000):
        diskon = 0.05
    else:
        diskon = 0
    total = belanja - (belanja * diskon)
    print(f"Total bayar: Rp{total:.0f}")

    # angka = int(input("Masukan Nilai: "))

    # print("Nilai : {}".format(angka))
    # if (angka < 0):
    #     angka *=-1
    #     print(f"Nilai : {angka}")

    # else: 
    #     print("Hraus bilangan positif")

    # if (angka > 0):
    #     print(f"Nilai bilangan positif")

    # elif(angka < 0): 
    #     print("Nilai bilangan negatif")

    # else:
    #     print("Angka Tersebut Bilangan Nol")


    # if (buah == "apel"):
    #     print(f"Makan buah {buah}")
    
    # elif (buah == "mangga"):
    #     print(f"Makan buah {buah}")

    # else:
    #     print("HARUS MAKAN BUAH!")
    
