angka = []

for i in range(10):
    nilai = int(input("Masukkan angka: "))
    angka.append(nilai)

terbesar = angka[0]

for i in range(10):
    if angka[i] > terbesar:
        terbesar = angka[i]

print("Bilangan terbesar =", terbesar)