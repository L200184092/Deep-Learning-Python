# Pencarian nama

daftar_nama = [ "Anwar Suadi", "Ahmad Jazuli", "Safitri", "Edi Junaedi", "Dian Anggraeni", "Rahmat Anwari" ]

dicari = input("Penggalan nama yang dicari : ")

indeks = 0
ditemukan = False

while indeks < len(daftar_nama):
    if dicari in daftar_nama[indeks]:
        ditemukan = True
        break

    else:
        indeks = indeks + 1

if ditemukan:
    print("Nama yang Anda cari cocok dengan : ", daftar_nama[indeks])
else:
    print("Tidak ada yang cocok")
