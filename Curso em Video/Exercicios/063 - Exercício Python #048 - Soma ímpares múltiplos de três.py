'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
no intervalo de 1 até 500
'''
lista = []
for n in range(1, 501, 2):
    if n % 3 == 0:
        lista.append(n)     
print(f"Quantidade de números na lista: [{len(lista)}]\n"
      f"Soma da lista atual: [{sum(lista)}]\n")


# for nota in notas:
#     soma_das_notas += nota

# print(soma_das_notas)