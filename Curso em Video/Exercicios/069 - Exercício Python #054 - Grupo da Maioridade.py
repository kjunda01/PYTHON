from datetime import date

ANO_ATUAL = date.today().year
cont_maior = 0
cont_menor = 0

for n in range(1, 8):
    galera = int(input(f"Em que ano a {n}ª pessoa nasceu? "))
    if galera <= ANO_ATUAL - 18:
        cont_maior += 1
        print(f"Essa pessoa [{n}] é MAIOR DE IDADE, tem {ANO_ATUAL - galera} anos.")
    else:
        cont_menor += 1
        print(f"Essa pessoa [{n}] é MENOR DE IDADE, tem {ANO_ATUAL - galera} anos.")
print(f"\nTivemos {cont_maior} pessoas maiores de idade e {cont_menor} pessoas menores de idade.")
