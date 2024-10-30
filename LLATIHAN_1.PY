from random import random
n = int(input("Masukkan nilai N: "))

for i in range(1, n + 1):
    angka_acak = random()
    if angka_acak < 0.5:
        print(f"data ke: {i} => {angka_acak}")
    else:
        while angka_acak >= 0.5:
            angka_acak = random()
        print(f"data ke: {i} => {angka_acak}")

print("Selesai")
