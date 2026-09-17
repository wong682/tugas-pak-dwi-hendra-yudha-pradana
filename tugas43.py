angka = []

for i in range(10):
    nilai = int(input("Masukkan angka: "))
    angka.append(nilai)

terkecil = angka[0]

for i in range(10):
    if angka[i] < terkecil:
        terkecil = angka[i]

print("Bilangan terkecil =", terkecil)