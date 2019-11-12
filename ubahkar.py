# ---------------------------------------
# ubahkar
#
# Contoh pengubahan karakter di file teks
# ---------------------------------------

# Buat file yang berisi ABCDEFGHIJ
berkas = open("kar.txt", "w")
berkas.write("ABCDEFGHIJ")
berkas.close()

# Buka file untuk operasi baca dan tulis
berkas = open("kar.txt", "r+")

# Tampilkan isinya
berkas.seek(0)
print(berkas.read())

# Lakukan perubahan
berkas.seek(5)
berkas.write("pqr")

# Tampilkan isinya
berkas.seek(0)
print(berkas.read())

berkas.close()
