lista = []
contador = 1

while True:

    notas = float(input("Digite a nota para média: "))
    lista.append(notas)
    print("Lista completa: ", * lista, sep= ", ")
    print(f"Nota {contador} adicionada. Para fazer a média digite -1")
    contador += 1

    if notas == -1:
        media = sum(lista[:-1]) / (contador-1)
        print(f"Média de {media}.")
        break
    