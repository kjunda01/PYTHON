from random import randint
from os import getlogin
usuario = getlogin() # Definir usuário para personalizar mensagem.

# Mensagem inicial
print("Sou seu computador...")
print("Acabei de pensar em um número entre 0 e 10.")
numero_computador = randint(0, 10) # Numero do pc para adivinhar

# Variáveis iniciais para o controle
palpite = ""
tentativas_maximas = 3 # colocar esse numero igual o tentativas restantes
tentativas_restantes = 3 # colocar esse numero igual o tentativas maximas
tentativas_gastas = 0

while palpite != numero_computador:
    print(f"\n{usuario}, suas tentativas restantes: {tentativas_restantes}")
    
    # validação de input do usuario, para aceitar somente numeros inteiros,
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            break
        except ValueError:
            print("Tentativa não contabilizada. Digite apenas números inteiros.")
        
    # Contadores para os cálculos de tentativas
    tentativas_restantes -= 1
    tentativas_gastas += 1

    # condicionais para verificar as tentativas
    if palpite == numero_computador:
        if tentativas_gastas == 1:
            print(f"{usuario}, Tu é o cara! Acertou de primeira! Boa!")
        elif tentativas_gastas == 3:
            print(f"{usuario}, foi no limite! Acertou na última tentativa. Parabéns!")
        else:
            print(f"Parabéns {usuario}! Você acertou! Gastou apenas {tentativas_gastas} tentativas.")
    
    if tentativas_restantes == 0 and palpite != numero_computador:
        print(f"Você infelizmente não adivinhou o número com as {tentativas_maximas} tentativas.")
        break

print("Saindo...")
