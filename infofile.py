# -----------------------------------------------------
# infofile
#
# Contoh untuk memperoleh informasi mengenai suatu file
# -----------------------------------------------------

import sys, os

if len(sys.argv) == 1:
    print("Penggunaan: infofile.py nama_file atau")
    print("infofile.py nama_direktori")
    sys.exit(1)

nama = sys.argv[1]
if os.path.isfile(nama):
    print("Merupakan nama file")
    print("Ukuran :", os.path.getsize(nama))
    print("Waktu terakhir dimodifikasi :", \
          os.path.getmtime(nama))
    print("Waktu terakhir diakses :", \
          os.path.getatime(nama))

if os.path.isdir(nama):
    print("Merupakan nama direktori")
