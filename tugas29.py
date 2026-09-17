n_awal = int(input("Masukkan bilangan awal: "))
n_akhir = int(input("Masukkan bilangan akhir: "))

for angka in range(n_awal, n_akhir + 1):
    if angka % 3 == 0:
        print(angka, end=" ")