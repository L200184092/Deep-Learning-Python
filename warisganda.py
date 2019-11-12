# ----------------------
# warisganda
#
# Contoh pewarisan ganda
# ----------------------

# Definisi kelas Ayah
class Ayah:
    motor = "Legenda"

# Definisi kelas Ibu
class Ibu:
    mobil = "Karimun"

# Kelas Anak mewarisi Ayah dan Ibu
class Anak(Ayah, Ibu):
    def info(self):
        print("Mobil :", self.mobil)
        print("Motor :", self.motor)

# Pembuatan objek
anak = Anak()

# Informasi objek
anak.info()
