#pertemuan 5 - quiz

#   Nama    = RAFI PRANATA
#   NPM     = 25670022 
#   KELAS   = 1A 

if __name__ == "__main__":
    tinggi_bola = float(input("Masukan Ketinggian Bola:  "))
    jml_pantulan = int(input("Masukan Jumlah Pantulan:  "))

    print(f"Tinggi Awal: {tinggi_bola}")

    for i in range(jml_pantulan):
        t = tinggi_bola / 2 
        print(f"Tinggi Pantulan ke-{i}: {t}")
        i += 1
    
    total_lintasan = tinggi_bola * jml_pantulan // 2
    print(f"Total Lintasan: {total_lintasan}")