"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Exemplo: Digite um número: 1834
Milhar: 1
Centena: 8 
Dezena: 3 
Unidade: 4

"""


numero = int(input("Digite um número: "))
verificar = len(str(numero))
numero = str(numero)

if verificar == 4:
    print(f'Unidade: {numero[0]}\nDezena: {numero[1]}\nCentena: {numero[2]}\nMilhar: {numero[3]}')
elif verificar == 3:
    print(f'Unidade: {numero[0]}\nDezena: {numero[1]}\nCentena: {numero[2]}\nMilhar: 0')
elif verificar == 2:
    print(f'Unidade: {numero[0]}\nDezena: {numero[1]}\nCentena: 0\nMilhar: 0')
else:
    print(f'Unidade: {numero[0]}\nDezena: 0\nCentena: 0\nMilhar: 0')


# numero = int(input("Digite um número: "))
# numero_str = str(numero)
# num_digits = len(numero_str)

# if num_digits > 4:
#     print("O número possui mais de quatro dígitos.")
# else:
#     unidades = int(numero_str[-1])
#     dezenas = int(numero_str[-2]) if num_digits >= 2 else 0
#     centenas = int(numero_str[-3]) if num_digits >= 3 else 0
#     milhares = int(numero_str[-4]) if num_digits == 4 else 0

#     print(f'Unidade: {unidades}\nDezena: {dezenas}\nCentena: {centenas}\nMilhar: {milhares}')
