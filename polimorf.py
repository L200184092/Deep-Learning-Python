# ----------------------
# polimorf
#
# Contoh pewarisan ganda
# ----------------------

# Definisi superkelas
class Kendaraan:
    def __init__(self, nama):
        self.nama = nama
    def jalankan(self):
        print("Silakan menjalankan", self.nama)

# Definisi subkelas
class Mobil(Kendaraan):
    def __init__(self):
        Kendaraan.__init__(self, "Mobil")

    def jalankan(self):
        print("Hidupkan mesin untuk menjalankan", self.nama)

# Definisi subkelas
class Sepeda(Kendaraan):
    def __init__(self):
        Kendaraan.__init__(self, "Sepeda")

    def jalankan(self):
        print("Kayuh pedal untuk menjalankan", self.nama)

# Definisi fungsi
def jalankanKendaraan(kendaraan):
    kendaraan.jalankan()

# Pembuatan objek
kendaraan = Kendaraan("Kendaraan Umum")
kendaraan.jalankan()

mobilku = Mobil()
mobilku.jalankan()

sepedaku = Sepeda()
sepedaku.jalankan()

# Pemanggilan dengan argumen berupa objek
print("\nTes menggunakan jalankanKendaraan():\n")
jalankanKendaraan(kendaraan)
jalankanKendaraan(mobilku)
jalankanKendaraan(sepedaku)
