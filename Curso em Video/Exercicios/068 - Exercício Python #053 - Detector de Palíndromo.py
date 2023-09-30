frase = input("Digite uma frase: ").upper().replace(" ", "")
inverso = frase.upper()[-1::-1]

print(f'O inverso de "{frase}" é "{inverso}".')
if frase == inverso:
    print("A frase digitada É SIM um palíndromo.")
else:
    print("A frase digitada NÃO é um palíndromo.")
