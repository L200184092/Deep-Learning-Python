# --------------------------------------
# bacapeg
#
# Contoh pembacaan data berbentuk record
#   dari file
# --------------------------------------

file_peg = open("pegawai.txt")

nip = file_peg.read(5)
while nip:
    nama = file_peg.read(20)
    gaji = file_peg.read(8)

    print(nip, nama, gaji)

    nip = file_peg.read(5)
