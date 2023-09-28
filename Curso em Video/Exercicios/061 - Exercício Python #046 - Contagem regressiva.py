#Contagem regressiva
from time import sleep

contagem = 10
while contagem > 0:
    print(contagem)
    sleep(1)
    contagem -= 1

print("FIM!")
