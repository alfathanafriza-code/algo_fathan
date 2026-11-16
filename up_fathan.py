print("APLIKASI PEMBAYARAN PARKIR")
print("Tarif: Motor = Rp2.000/jam  | Mobil = Rp5.000/jam | Bus = 10.000/jam")
print("jika parkir > 5 jam, tambah Rp5.000")

jumlah = int(input("\nMasukkan jumlah kendaraan: "))

for i in range(1, jumlah + 1):
    print(f"\n--- Kendaraan ke-{i} ---")

    jenis = input("Jenis kendaraan (motor/mobil/bus): ").lower()
    lama = int(input("Lama parkir (jam): "))
    
    if jenis == "motor":
        tarif = 2000
    elif jenis == "mobil":
        tarif = 5000
    elif jenis == "bus":
        tarif = 10000
    else:
        print("Jenis kendaraan tidak valid")
        continue

    biaya = tarif * lama

    if lama > 5:
        biaya_tambahan = 5000
    else:
        biaya_tambahan = 0

    total = biaya + biaya_tambahan

    print(f"Jenis Kendaraan : {jenis}")
    print(f"Lama Parkir     : {lama} jam")
    print(f"Biaya Parkir    : Rp{biaya:,}")
    print(f"TOTAL BAYAR     : Rp{total:,}")
    print("-----------------------------")

print("\nTerima kasih, selamat jalan!")