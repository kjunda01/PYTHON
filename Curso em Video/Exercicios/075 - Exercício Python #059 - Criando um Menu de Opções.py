def numero_formatado(numero):
    if numero == int(numero):
        return int(numero)
    else:
        return numero

def formatacao():
    print("=" * 22)
    print("Digite penas números.")
    print("=" * 22)

def numero1():
    while True: # OBTER VALOR 1
        try:
            val1 = float(input("\nPRIMEIRO VALOR: "))
            return val1
        except ValueError:
            formatacao()

def numero2():
    while True: # OBTER VALOR 1
        try:
            val1 = float(input("SEGUNDO VALOR: "))
            return val1
        except ValueError:
            formatacao()


val1 = numero_formatado(numero1())
val2 = numero_formatado(numero2())
menu = 0
while menu != 5:
    while True:
        try:
            menu = int(input("\n*** MENU INTERATIVO ***\n[0] - Mostrar números atuais\n[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - SAIR\nOpção: "))
            break
        except ValueError:
            print("\nDigite apenas as opções indicadas.\n")
    
    if menu == 0:
        print(f"\n{'=' * 22}\nPrimeiro valor: {val1}")
        print(f"Segundo valor: {val2}\n{'=' * 22}")
    
    elif menu == 1:
        print(f"\nResposta: {val1} + {val2} = {numero_formatado(val1 + val2)}")

    elif menu == 2:
        print(f"\nResposta: {val1} x {val2} = {numero_formatado(val1 * val2)}")

    elif menu == 3:
        lista = []
        lista.append(val1), lista.append(val2)
        lista.sort()
        print(f"\nResposta: O maior número dos valores {val1} e {val2} é: {lista[-1]}")

    elif menu == 4:
        numero1()
        numero2()

print("\nSaindo do programa....\n")

