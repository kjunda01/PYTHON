"""

Crie um programa que leie o nome de uma pessoa e diga se ela tem "SILVA" no nome.

"""

nome = input("Digite seu nome completo: ").upper()
primeiro_nome = nome.split(" ")[0].upper()
print(f"Vamos conferir.")
print(f'{primeiro_nome}, seu nome possui SILVA.') if "SILVA" in nome else print("Não possui SILVA no nome.")
