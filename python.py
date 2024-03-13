def hitung_gaji():
    nama_karyawan = input("Nama karyawan: ")
    gaji_pokok = float(input("Gaji pokok: "))
    jam_kerja_per_hari = int(input("Jumlah jam kerja per hari: "))
    
    while True:
        pilihan = input("Pilih Rincian Gaji (1 untuk Harian, 2 untuk Mingguan): ")
        if pilihan == '1':
            gaji_harian = gaji_pokok / 8
            print(f"Gaji harian {nama_karyawan} adalah: {gaji_harian}")
            break
        elif pilihan == '2':
            gaji_mingguan = gaji_pokok / 48
            print(f"Gaji mingguan {nama_karyawan} adalah: {gaji_mingguan}")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

hitung_gaji()
