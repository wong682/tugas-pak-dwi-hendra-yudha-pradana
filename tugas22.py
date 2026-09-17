def tampilkan_faktorial(n):
    if n < 0:
        return "Faktorial tidak terdefinisi untuk bilangan negatif."

    angka = [str(i) for i in range(n, 0, -1)]

    hasil = 1
    for i in range(n, 0, -1):
        hasil *= i

    perkalian = " x ".join(angka)

    return f"{n}! = {perkalian} = {hasil}"

n = 4

print(tampilkan_faktorial(n))