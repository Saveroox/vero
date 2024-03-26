def hitung_diskon(total_belanja):
    if total_belanja >= 250000:
        diskon = total_belanja * 50 / 100
        return diskon
    else:
        return 0

def main():
    total_belanja = float(input("Masukkan total belanja Anda: Rp "))
    diskon = hitung_diskon(total_belanja)

    if diskon > 0:
        print("Selamat! Anda mendapatkan diskon sebesar Rp.", diskon)
    else:
        print("Total belanjaan Anda: Rp.", total_belanja)
        print("Maaf, Anda tidak mendapatkan diskon karena total belanjaan tidak mencapai Rp. 250.000.")

if __name__ == "__main__":
    main()
