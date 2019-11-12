# Penentuan skor
# Versi 2

nilai = input("Nilai ujian (0-100) : ")
nilai = int(nilai)

if nilai >= 90:
    print("A")
elif 70 <= nilai < 90:
    print("B")
elif 60 <= nilai < 70:
    print("C")
elif 50 <= nilai < 60:
    print("D")
else:
    print("E")
