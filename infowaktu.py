# ---------------------------------------
# infowaktu
#
# Contoh untuk memperoleh informasi waktu
# ---------------------------------------

import time

bulan = ("Januari", "Februari", "Maret",
         "April", "Mei", "Juni",
         "Juli", "Agustus", "September",
         "Oktober", "November", "Desember")
hari = ("Minggu", "Senin", "Selasa",
        "Rabu", "Kamis", "Jumat", "Sabtu")

sekarang = time.time()
infowaktu = time.localtime(sekarang)
print("Saat sekarang:")
print("Tanggal", infowaktu[2], \
      bulan[infowaktu[1] - 1], infowaktu[0])

print("Hari", hari[infowaktu[6]])
print("Jam", str(infowaktu[3]) + ":" + \
            str(infowaktu[4]) + ":" + \
            str(infowaktu[5]))
