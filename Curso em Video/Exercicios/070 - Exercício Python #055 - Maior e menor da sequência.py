lista = []

for n in range(1, 6):
    peso = float(input(f"Peso da {n}ª pessoa: "))
    lista.append(peso)

lista.sort()

print(f"O MAIOR peso foi de {lista[-1]}Kg.")
print(f"O MENOR peso foi de {lista[0]}Kg.")
