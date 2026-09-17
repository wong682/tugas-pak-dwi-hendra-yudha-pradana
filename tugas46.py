n_awal = int(input("Masukkan bilangan awal: "))
n_akhir = int(input("Masukkan bilangan akhir: "))

jumlah = 0

for i in range(n_awal, n_akhir + 1):
    if i > 0:
        jumlah = jumlah + i

print("Jumlah bilangan positif =", jumlah)