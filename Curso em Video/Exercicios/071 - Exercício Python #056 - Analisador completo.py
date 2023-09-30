lista_nome = []
lista_idade = []
lista_sexo = []

for n in range(4):
    print(f"\n----- {n + 1}ª PESSOA -----")

    # nome = input("Nome: ")
    # lista_nome.append(nome)

    idade = int(input("Idade: "))
    lista_idade.append(idade)

    # sexo = input("Sexo [M/F]: ").capitalize()[0]
    # lista_sexo.append(sexo)

media_idade = sum(lista_idade) / len(lista_idade)
print(f"A média da idade do grupo é de {media_idade:.0f} anos.")

