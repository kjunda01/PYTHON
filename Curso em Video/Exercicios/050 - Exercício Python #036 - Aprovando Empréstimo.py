"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salário do comprador? "))
anos = int(input("Quantos anos deseja pagar? "))

prestacao = valor_casa / (anos * 12)

limite = 30/100 * salario

def moeda(real):
    dinheiro = f'R${real:,.2f}'.replace(',', ' ').replace('.', ',').replace(' ', '.')
    return  dinheiro

if prestacao >= limite:
    print(f"A prestação de {moeda(prestacao)} passou de 30% do salário -> {moeda(limite)}.\nEmpréstimo não realizado.")

else:
    print(f"Empréstimo aceito.")
