print("\nCari Volume Dengan Def")


def volume(a, b):
    hasil = ((a/2)*(a/2))*3.14*b
    print(hasil)


a = 20
b = 28
volume(a, b)
# ===============================================

print("\nCari Keliling Dengan Lambda")


def keliling(sisi): return sisi*3


print(keliling(50))
# ===============================================

print("\nHitung Kalkulator")


class Kalkulator:
    def __init__(obj, angka1, angka2):
        obj.angka1 = angka1
        obj.angka2 = angka2

    def pertambahan(tambah):
        hasil = tambah.angka1 + tambah.angka2
        print(str(tambah.angka1) + " + " +
              str(tambah.angka2) + " = " + str(hasil))

    def pengurangan(kurang):
        hasil = kurang.angka1 - kurang.angka2
        print(str(kurang.angka1) + " - " +
              str(kurang.angka2) + " = " + str(hasil))

    def pembagian(bagi):
        hasil = bagi.angka1 / bagi.angka2
        print(str(bagi.angka1) + " / " + str(bagi.angka2) + " = " + str(hasil))

    def perkalian(kali):
        hasil = kali.angka1 * kali.angka2
        print(str(kali.angka1) + " * " + str(kali.angka2) + " = "+str(hasil))


a2 = Kalkulator(8, 4)
a2.pertambahan()
a2.pengurangan()
a2.pembagian()
a2.perkalian()


# Berdasarkan Inputan


print("\n")

# Mencari Volume
# print("\nCari Volume Dengan Def")

nilai_a = int(input("Masukan Nilai 1 : "))
nilai_b = int(input("Masukan Nilai 2 : "))
volume = ((nilai_a/2)*(nilai_a/2))*3.14*nilai_b

print("Maka Hasil Volume = > " + str(volume))

# =====================================================


print("\n")

# Mencari Keliling Lingkaran
# print("\nCari Keliling Dengan Lambda")

sisi = int(input("Masukan Panjang Sisi Segitiga : "))
keliling = sisi*3

print("Keliling Dari Segitiga Tersebut : " + str(keliling))


# ========================================================

print("\n")

# Kalkulator

angkaa = int(input("Masukan Angka 1 : "))
angkab = int(input("Masukan Angka 2 : "))





perhitungan = input("Masukan Operator Hitung : ")
if (perhitungan == f"+"):
    hasil = angkaa + angkab
elif (perhitungan == f"-"):
    hasil = angkaa - angkab
    print(hasil)
elif (perhitungan == f"*"):
    hasil = angkaa * angkab
    print(hasil)
elif (perhitungan == f"/"):
    hasil = angkaa / angkab
    print(hasil)
