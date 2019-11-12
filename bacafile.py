# -----------------------------
# bacafile
#
# Contoh operasi pembacaan file
# -----------------------------

file = open("kota.txt")
baris = file.readline()

# buang newline di akhir string
baris = baris[:-1]

while baris:
    print(baris)
    baris = file.readline()
    baris = baris[:-1]

file.close()
