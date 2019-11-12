# Penentuan skor

nilai = input("Nilai ujian (0 - 100) : ")
nilai = int(nilai)

if nilai >= 90:
    print("A")
elif nilai >=70:
    print("B")
elif nilai >= 60:
    print("C")
elif nilai >50:
    print("D")
else:
    print("E")
