def konversi_bilangan(angka):
    return bin(angka), oct(angka), hex(angka)

if __name__ == "__main__":
    angka_desimal = int(input("Masukkan bilangan desimal: "))

    biner, oktal, heksa = konversi_bilangan(angka_desimal)

    print(f"Bilangan biner: {biner}")
    print(f"Bilangan oktal: {oktal}")
    print(f"Bilangan heksadesimal: {heksa}")