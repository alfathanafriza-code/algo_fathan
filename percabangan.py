# input
nilai = int(input("Masukkan nilai:"))
# proses
if nilai >=80 and nilai<=100:
    print("Anda Mendapatkan Nilai A")
elif nilai >=70 and nilai <=80:
    print("Anda Mendapatkan Nilai B")
elif nilai >=50 and nilai <=70:
    print("Anda Mendapatkan Nilai C")
elif nilai >=30 and nilai <=50:
    print("Anda Mendapatkan Nilai D")
elif nilai >=0 and nilai <=20:
    print("Anda Mendapatkan Nilai E")
else:
    print("Data tidak valid")
print("==========Latihan==========")

Barang = input("Masukkan nama barang:")
Harga = int(input("Masukkan harga barang:"))

if Barang == "kulkas" :
    print (Barang)
    print ( Harga - (Harga * 0.10))
elif Barang == "TV" :
    print (Barang)
    print ( Harga - (0.05 * Harga))
else:
    print (Barang)
    print (Harga)

