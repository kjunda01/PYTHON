numero = int(input("Digite um número: "))

lista = []

if numero > 1:
    for contador in range(1,numero + 1):
        if numero % contador == 0:
            lista.append(contador)
    
    if len(lista) > 2:
        print(f"O número {numero} não é primo porque possui {len(lista)} divisores.\n"
              f"Divisores: {', '.join(map(str, lista))}.")
    else:
        print(f"{numero} é divisível somente por 1 e por {numero}, portanto É PRIMO.")
