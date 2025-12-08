#pertemuan 13 - Sorting

#   Nama    = RAFI PRANATA
#   NPM     = 25670022 
#   KELAS   = 1A 

def bubble_sort(data):
    for i in range(0, len(data)-1):
        for j in range(0, len(data)-i-1):
            if (data[j] > data[j+1]):
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

def cetak_list(data):
    for item in data:
        print(item,end="")
    print("")