def hitung_nilai_akhir(kehadiran, tugas, uts, uas):
    total_kehadiran = kehadiran * 16
    total_tugas = sum(tugas)
    nilai_akhir = total_kehadiran + total_tugas + uts + uas
    return nilai_akhir

def tentukan_hasil_nilai(nilai_akhir):
    if nilai_akhir >= 90:
        return "A"
    elif nilai_akhir >= 80:
        return "B"
    elif nilai_akhir >= 70:
        return "C"
    elif nilai_akhir >= 60:
        return "D"
    else:
        return "E"

def main():
    kehadiran = int(input("Masukkan jumlah kehadiran: "))
    tugas = [float(input("Masukkan nilai tugas ke-" + str(i+1) + ": ")) for i in range(8)]
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    nilai_akhir = hitung_nilai_akhir(kehadiran, tugas, uts, uas)
    hasil_nilai = tentukan_hasil_nilai(nilai_akhir)

    print("Nilai akhir mahasiswa:", nilai_akhir)
    print("Hasil kelulusan:", hasil_nilai)

if __name__ == "__main__":
    main()
