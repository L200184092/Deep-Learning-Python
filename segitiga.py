# Cara membuat segitiga bintang
# yang bersifat variabel

tinggi = input("Tinggi segitiga : ")
tinggi = int(tinggi)

baris = 1
while baris <= tinggi :
    kolom = 1
    while kolom <= baris:
        print("*", end = " ")
        kolom = kolom + 1
    print(" ")
    baris = baris + 1
