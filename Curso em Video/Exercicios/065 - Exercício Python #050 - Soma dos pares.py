'''
Desenvolva um programa que leia 6 número inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado por ímpar, desconsidere-o.
'''


lista = []
lista_pares = []
NUMEROS_MAXIMOS = 5

while len(lista) <= NUMEROS_MAXIMOS:# Vai pedir 6 números
    try:
        numero = int(input("Digite um número inteiro: "))
        lista.append(numero) # Vai colocar todos os números em uma lista, pra usar todos de uma vez depois.
    except:
        print("Digite apenas NÚMEROS INTEIROS.")

contador = 0
for numeros in lista:
    if numeros % 2 == 0:
        lista_pares.append(numeros) # Vai acrescentar somente os números pares na lista nova
        contador += 1
    
soma_pares = sum(lista_pares)
print(f"Você informou {contador} números pares e a soma foi: {soma_pares}") # Faz a soma dos números pares da lista.


