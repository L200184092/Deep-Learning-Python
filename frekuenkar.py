# ---------------------------------------------
# frekuenkar
# 
# Contoh untuk menghitung frekuensi karakter
#   dalam suatu string dengan memanfaatkan list
# ---------------------------------------------

kalimat = input("Masukkan suatu kalimat: ")
jumkar = {}
for kar in kalimat:
    jumkar[kar] = jumkar.get(kar,0) + 1

# Tampilkan frekuensi karakter
for kar in jumkar.keys():
    if kar == " ":
        print("Spasi = ", end = " ")
    else:
        print(kar, "=", end = " ")

    print(jumkar[kar])
