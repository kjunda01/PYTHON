"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

"""
 
kms = float(input("Digite a distância da sua viagem: "))

passagem = 0.50 if kms <= 200 else 0.45

print(f"Para uma viagem de {kms:.2f} quilômetros, você pagará R${kms*passagem}".replace(".",","))

