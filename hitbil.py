daftar = ["1234", 2, "Edi", 1999]
jumlah = 0

for nilai in daftar:
    try:
        bil = int(nilai)
        jumlah = jumlah + 1
    except ValueError:
        pass

print("Jumlah elemen berupa bilangan:", jumlah)
