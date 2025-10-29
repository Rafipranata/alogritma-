#pertemuan 6-7 - If Nested

#   Nama    = RAFI PRANATA
#   NPM     = 25670022 
#   KELAS   = 1A 

if __name__ == "__main__":
    harga = 0
    print("============Pengiriman Logistik============")
    print("Pilih Jenis Pengirimaan :")
    print("1. Domestik ")
    print("2. Internasional ")
    jenis = input("Masukan Jenis Pengiriman: ")

    if(jenis == "domestik" or jenis == "Domestik" or jenis == "DOMESTIK"):
        print("=======Jenis Paket Pengiriman Domestik======")
        print("1. Next Day (1 Hari): Rp.30.000")
        print("2. Reguler (3-5 Hari): Rp.18.000")
        print("3. Kargo (5-7 Hari): Rp.12.000")
        print("========================")
        paket = int(input("Masukan Pilihian Anda (1 - 3): "))
        if(paket == 1):
            harga = 30000
            print("Anda Memilih Paket Next Day")
            print("Dengan Harga Rp. 30.000 per Kg")
        elif(paket == 2):
            harga = 18000
            print("Anda Memilih Paket Reguler")
            print("Dengan Harga Rp. 18.000 per Kg")
        elif(paket == 3):
            harga = 12000
            print("Anda Memilih Paket Kargo")
            print("Dengan Harga Rp. 12.000 per Kg")
        else:
            print("Pilihan Anda Tidak Valid! ")
        
    elif(jenis == "internasional" or jenis == "Internasional" or jenis == "INTERNASIONAL"):
        print("=======Jenis Paket Pengiriman Internasional======")
        print("1. Asia Tenggara: Rp.200.000")
        print("2. Asia/Australia: Rp.300.000")
        print("3. Amerika: Rp.500.000")
        print("4. Eropa: Rp.800.000")
        print("========================")
        paket = int(input("Masukan Pilihian Anda (1 - 4): "))
        if(paket == 1):
            harga = 200000
            print("Anda Memilih Paket Asia Tenggara")
            print("Dengan Harga Rp. 200.000 per Kg")
        elif(paket == 2):
            harga = 300000
            print("Anda Memilih Paket Asia/Australia")
            print("Dengan Harga Rp. 300.000 per Kg")
        elif(paket == 3):
            harga = 500000
            print("Anda Memilih Paket Amerika")
            print("Dengan Harga Rp. 500.000 per Kg")
        elif(paket == 4):
            harga = 800000
            print("Anda Memilih Paket Eropa")
            print("Dengan Harga Rp. 800.000 per Kg")
        else:
            print("Pilihan Anda Tidak Valid! ")

    else:
        print("Jenis Pengiriman Tidak Valid! ")

    if(harga > 0):
        berat = float(input("Masukan Berat Barang: "))
        total_bayar = harga * berat
        print("Total Biaya yang Harus Anda Bayar: Rp. %.0f" %(total_bayar))