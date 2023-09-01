def somarnotas(quantidade):
    soma  = 0
    numero = 1
    while numero <= quantidade:
        soma += numero
        numero += 1
    return soma

print(somarnotas(6))

print(somarnotas(1000))