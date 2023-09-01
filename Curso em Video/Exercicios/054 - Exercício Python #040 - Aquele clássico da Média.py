lista = []
contador = 1
soma_das_notas = 0

while True:
    notas = int(input(f"Para fazer a média digite um número negativo.\n\n"
                  f"Nota: "))
    lista.append(notas)
    lista.sort()
    print(f"A nota de número [{contador}] foi adicionada.\n")
    contador += 1
    if lista[0] < 0:
        lista.remove(lista[0])
        print("Lista completa:")
        print(*lista, sep=(", "))
        print(f"\nMédia das {contador - 2} notas: {(sum(lista)) / (contador - 2)}")
        break