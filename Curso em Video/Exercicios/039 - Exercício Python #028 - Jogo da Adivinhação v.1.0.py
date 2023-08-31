"""


"""
from random import randint

print("-="*31)
print("   Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-="*31)



num_pc = randint(0,5)
tentativas = 1
while True:
    num_user = int(input("Digite um número entre 0 e 5: "))

    if num_user == num_pc:
        print(f"Parabéns, você acertou! Gastou {tentativas} tentativas.")
        tentativas += 1
        break

    else:
        print(f"Gastou {tentativas} tentativa.\nDigite novamente o número para tentar.")
        tentativas += 1

print("Que legal, você me venceu... Até a próxima!!!")

