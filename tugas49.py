n_awal = int(input("Masukkan bilangan awal: "))
n_akhir = int(input("Masukkan bilangan akhir: "))

for angka in range(n_awal, n_akhir + 1):
    jumlah = 0

    for i in range(1, angka + 1):
        if angka % i == 0:
            jumlah = jumlah + 1

    if jumlah == 2:
        print(angka, end=" ")