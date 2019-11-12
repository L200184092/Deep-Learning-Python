#contoh penggunaan operator // dan %
	
total_detik = 10000

jumlah_jam = total_detik // 3600
jumlah_menit = (total_detik //60) % 60
sisa_detik = total_detik % 60

print("Total jam = ", jumlah_jam)
print("Total menit = ", jumlah_menit)
print("Sisa detik = ", sisa_detik)