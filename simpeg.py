# ----------------------------------------
# simpeg
#
# Contoh penyimpanan data berbentuk record
#   ke file
# ----------------------------------------

daftar_pegawai = [
    ("11234", "Amir Hamzah", 2200000),
    ("11235", "Fatimah", 1300000),
    ("11236", "Fika Ariyanti", 800000),
    ("11237", "Dewi Fadlilah", 1300000),
    ("11238", "Joni Ardian", 700000)]

file_peg = open("pegawai.txt", "w")

for pegawai in daftar_pegawai:
    format = "%-5s%-20s%8d" % \
             (pegawai[0], pegawai[1], pegawai[2])
    file_peg.write(format)

file_peg.close()

print("Data pegawai telah disimpan di pegawai.txt")
