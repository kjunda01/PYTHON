"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
"""

cidade = input("Digite a cidade em que você nasceu: ")

conferir = cidade.upper()

if conferir[0:4] == 'SANTO' or "SÃO":
    print(f'A sua cidade {conferir} começa com "Santo"')
else:
    print(f'{conferir} não começa com "Santo"')
