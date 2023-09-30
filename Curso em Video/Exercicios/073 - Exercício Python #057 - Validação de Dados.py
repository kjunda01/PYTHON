contador = 1
sexo = input("Informe seu sexo - [M/F]: ").strip().upper()[0]

while sexo not in "MmFf":
    print(f"Tentativa de número {contador + 1}")
    sexo = input("Dados inválidos. Informe um sexo válido: ").strip().upper()[0]
    contador += 1

print(f"Foram necessárias {contador} tentativas.")
print(f"Sexo: {sexo}. Continuando...")
print("Fim do programa")
