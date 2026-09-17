angka = []

for i in range(10):
    nilai = int(input("Masukkan angka: "))
    angka.append(nilai)

jumlah_ganjil = 0

for i in range(10):
    if angka[i] % 2 != 0:
        jumlah_ganjil = jumlah_ganjil + 1

print("Jumlah bilangan ganjil =", jumlah_ganjil)