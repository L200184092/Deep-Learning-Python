# ------------------------------------
# hitluas
# Contoh skrip yang mendefinisikan
#   dua fungsi
# ------------------------------------

def hitung_luas_lingkaran():
    print("Menghitung luas lingkaran")
    radius = input("Jari-jari = ")
    radius = int(radius)
    luas = 3.14 * radius * radius
    print("Luas =", luas)

def hitung_luas_persegipanjang():
    print("Menghitung luas persegi panjang")
    panjang = input("Panjang = ")
    panjang = int(panjang)
    lebar = input("Lebar = ")
    lebar = int(lebar)
    luas = panjang * lebar
    print("Luas =", luas)

# Program utama
print("Menghitung luas")
print("1. Lingkaran")
print("2. Persegipanjang")

pilihan = input("Pilihan (1 atau 2): ")
if pilihan == "1":
    hitung_luas_lingkaran()
elif pilihan == "2":
    hitung_luas_persegipanjang()
else:
    print("Pilihan salah")
