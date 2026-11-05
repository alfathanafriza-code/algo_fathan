jumlah = int(input("Jumlah mahasiswa (5-10): "))

if jumlah < 5 or jumlah > 10:
    print("Jumlah harus antara 5 sampai 10!")
else:
    total = 0
    
    for i in range(1, jumlah + 1):
        nilai = float(input(f"Masukkan Nilai mahasiswa {i}: "))
        total += nilai

    # 4. Hitung rata-rata
    rata_rata = total / jumlah
    
    print("\n-------------------------")
    print(f"Nilai rata - rata : {rata_rata:.2f}")

    # Tambahan biar nilai lebih bagus (pakai IF lagi untuk grade)
    if rata_rata >= 85:
        print("Kategori: A (Sangat Baik)")
    elif rata_rata >= 70:
        print("Kategori: B (Baik)")
    elif rata_rata >= 60:
        print("Kategori: C (Cukup)")
    else:
        print("Kategori: D (Kurang)")