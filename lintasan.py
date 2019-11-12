# --------------------------------------------------
# lintasan
#
# Contoh penggunaan metode sin() dan cos() pada math
# --------------------------------------------------

import math

kecepatan = input("Kecepatan: ")
sudut = input("Sudut (derajat): ")

# Konversi ke float
kecepatan = float(kecepatan)
sudut = float(sudut)

# Perhitungan
sudut = math.radians(sudut)
jarak = 2 * kecepatan * kecepatan * \
        math.sin(sudut) * math.cos(sudut) / 9.8

print("Jarak =", jarak)
