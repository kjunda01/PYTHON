"""
Crie um programa que leia um número inteiro e diga na tela se ele é PAR ou ÍMPAR

"""

while True:
    try:
        num = float(input("Digite um número: "))
        if num % 2 == 0:
            print(f"O número {num} é PAR")
            break
        else:
            print(f"O número {num} é ÍMPAR")
            break
    except ValueError:
        print("Digite apenas números.")
