# ----------------------------------
# cekpar
# 
# Pemeriksaan argumen baris perintah
# ----------------------------------

import sys

if len(sys.argv) == 1:
    print("Penggunaan: cekpar.py arg1 arg2 ...")
    sys.exit(1)

print("Hasil sys.argv: ")
print(sys.argv)

sys.exit(0)
