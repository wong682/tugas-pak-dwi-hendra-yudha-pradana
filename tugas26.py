n_awal = int(input("45"))
n_akhir = int(input("2024 "))

for tahun in range(n_awal, n_akhir + 1):
    if tahun % 4 == 0 and tahun % 10 == 4:
        print(tahun, end=" ")