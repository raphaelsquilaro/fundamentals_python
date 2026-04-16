# Author: Raphael Campos Squilaro


i = 1
while i <= 10:
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')
    print()  # Imprime uma linha em branco para separar as tabuadas
    i += 1

x = 1
while x <= 10:
    for y in range(1, 11):
        for z in range(1, 11):
            print(f'{x} x {y} x {z} = {x * y * z}')
        print()  # Imprime uma linha em branco para separar as tabuadas
    x += 1

a = 1
while a <= 10:
    for b in range(1, 11):
        for c in range(1, 11):
            for d in range(1, 11):
                print(f'{a} x {b} x {c} x {d} = {a * b * c * d}')
            print()  # Imprime uma linha em branco para separar as tabuadas
    a += 1


e = 1
while e <= 10:
    for f in range(1, 11):
        for g in range(1, 11):
            for h in range(1, 11):
                for i in range(1, 11):
                    print(f'{e} x {f} x {g} x {h} x {i} = {e * f * g * h * i}')
                print()  # Imprime uma linha em branco para separar as tabuadas
    e += 1


    