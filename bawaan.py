# ----------------------------------
# bawaan
#
# Contoh argumen dengan nilai bawaan
# ----------------------------------

# Definisi kelas
class Buku:
    def __init__(self, judul="", pengarang=""):
        self.judul = judul
        self.pengarang = pengarang

    def info(self):
        print("Judul : ", self.judul)
        print("Pengarang : ", self.pengarang)
        print("")

# Pembuatan objek
bukuA = Buku("Pemrograman Python", "Abdul Kadir")
bukuB = Buku("Referensi C++")
bukuC = Buku()

# Info Buku
print("BukuA:")
bukuA.info()

print("BukuB:")
bukuB.info()

print("BukuC:")
bukuC.info()
