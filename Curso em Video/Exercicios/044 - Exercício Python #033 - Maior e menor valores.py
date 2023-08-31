"""


"""

listaNumeros = []

while True:

    numeros = int(input("Digite um número: "))

    if numeros == 000:
        print("Lista completa: ", * listaNumeros, sep = ", ")
        print(f"Saindo...")
        break

    elif numeros != 0:
        listaNumeros.append(numeros)
        print(f"Lista completa: {listaNumeros}")
        listaNumeros.sort()
        print(f"Maior número da lista = ({listaNumeros[-1]}).")
        print(f"Menor número da lista = ({listaNumeros[0]}).")
        

