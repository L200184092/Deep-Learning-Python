# ----------------------------------------------
# robot
#
# Contoh kelas dengan konstruktor dan destruktor
# ----------------------------------------------

class Robot:
    jumlah_hidup = 0 # Variabel kelas

    # ----- konstruktor
    def __init__(self, nama):
        self.nama = nama
        Robot.jumlah_hidup += 1

    # ----- desktruktor
    def __del__(self):
        Robot.jumlah_hidup -= 1

    # ----- metode
    def info(self):
        print("Robot :", self.nama)
        print("Robot hidup:", Robot.jumlah_hidup)
        print("")

# Penciptaan objek
robotA = Robot("Arjuna")
robotB = Robot("Birowo")
robotC = Robot("Cucakrowo")

# Pemanggilan metode
print("Informasi untuk robotA:")
robotA.info()

print("Informasi untuk robotB:")
robotB.info()

print("Informasi untuk robotC:")
robotC.info()

# Pemeriksaan atribut jumlah_hidup
print("Setelah tiga objek diciptakan")
print("jumlah_hidup = ", Robot.jumlah_hidup)
print("")

# Penghapusan satu objek
del(robotB)

print("Setelah objek yang dirujuk robotB dihapus:")
print("jumlah_hidup = ", Robot.jumlah_hidup)
