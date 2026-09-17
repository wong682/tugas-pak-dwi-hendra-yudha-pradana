angka = []

for i in range(10):
    nilai = int(input("Masukkan angka: "))
    angka.append(nilai)

jumlah_genap = 0

for i in range(10):
    if angka[i] % 2 == 0:
        jumlah_genap = jumlah_genap + 1

print("Jumlah bilangan genap =", jumlah_genap)