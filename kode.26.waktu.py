# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput Satuan Jarak
jam = float(input("Tuliskan Berapa Jam: "))

# Mengkonversi
hari  = jam / 24
minggu  = hari / 7
bulan = minggu / 4
tahun = bulan / 12
 
# Menampilkan Hasil 
print('%d  Jam sama dengan %d Hari' %(jam,hari))
print('%d  Jam sama dengan %d Minggu' %(jam,minggu))
print('%d  Jam sama dengan %d Bulan' %(jam,bulan))
print('%d  Jam sama dengan %d Tahun' %(jam,tahun))
