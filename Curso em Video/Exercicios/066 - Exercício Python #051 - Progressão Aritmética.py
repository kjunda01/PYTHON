'''
An = a1 + (n - 1) * r
an: termo que queremos calcular
a1: primeiro termo da P.A.
n: posição do termo que queremos descobrir
r: razão
'''

print(('=' * 30).center(30))
print("10 TERMOS DE UMA PA".center(30))
print(('=' * 30).center(30))

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
contador = 0
for n in range(1, 11):
    pa = primeiro_termo + (n - 1) * razao
    contador += 1
    print(pa, end=" ► ")
    if contador == 10:
        print(f"ACABOU")

