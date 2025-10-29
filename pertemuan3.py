#pertemuan 2 - Operator

#   Nama    = RAFI PRANATA
#   NPM     = 25670022
#   KELAS   = 1A 

if __name__ == "__main__":
    angka1 = 25
    angka2 = 5
    # Operator Aritmatika
    perkalian = angka1 * angka2 
    pembagian = angka1 / angka2 
    penambahan = angka1 + angka2 
    pengurangan = angka1 - angka2 
    sisabagi = angka1 % angka2

    print(f"Hasil Perkalian {angka1} x {angka2} = {perkalian} ")
    print(f"Hasil Pembagian {angka1} / {angka2} = {pembagian} ")
    print(f"Hasil Penambahan {angka1} + {angka2} = {penambahan} ")
    print(f"Hasil Pengurangan {angka1} - {angka2} = {pengurangan} ")
    print(f"Hasil Sisa Bagi {angka1} % {angka2} = {sisabagi} ")

    print("Operator Aritmatika")
    print("======================================================")

    #Operator Relational
    lebihkecil = angka1 < angka2
    lebihbesar = angka1 > angka2
    lebih_besar_sama_dengan =  angka1 >= angka2
    lebih_kecil_sama_dengan = angka1 <= angka2
    sama_dengan = angka1 == angka2
    tidak_sama_dengan = angka1 != angka2
    print(f" {angka1} < {angka2} = {lebihkecil} ")
    print(f" {angka1} > {angka2} = {lebihbesar} ")
    print(f" {angka1} >= {angka2} = {lebih_besar_sama_dengan} ")
    print(f" {angka1} =< {angka2} = {lebih_kecil_sama_dengan} ")
    print(f" {angka1} == {angka2} = {sama_dengan} ")
    print(f" {angka1} != {angka2} = {tidak_sama_dengan} ")

    print("Operator Relational")
    print("======================================================")

    boolean1 = True
    boolean1 =  False

    angka3 = 15

    hasil = (angka3 >= 20) and (angka3 % 3 != 0)
    print(hasil)

    print("Operator Logika")
    print("======================================================")

    angka1 = 25
    angka2 = 5
    # Operator Penugasan
    angka1 *= angka2
    print(angka1)
    # angka1 /= angka2 
    # angka1 += angka2 
    # angka1 -= angka2 
    # angka1 %= angka2
    print("Operator Penugasan")
    print("======================================================")