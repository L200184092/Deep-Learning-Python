# ----------------------
# pewarisan
#
# Contoh pewarisan kelas
# ----------------------

# Kelas dasar
class Buku:
    def __init__(self, judul = "", pengarang = ""):
        self.judul = judul
        self.pengarang = pengarang
    def info(self):
        print("Judul :", self.judul)
        print("Pengarang :", self.pengarang)

# Subkelas
class BukuFiksi(Buku):
    def __init__(self, judul = "", pengarang = "", tokoh = []):
        Buku.__init__(self, judul, pengarang)
        self.tokoh = tokoh
    def info(self):
        Buku.info(self)
        print("Tokoh :", self.tokoh)

# Pembuatan objek
novel = BukuFiksi("Penculikan Kalkulus",
                  "Herge", ["Tintin", "Prof. Kalkulus"])
novel.info()
