"""


"""
######################### VERSÃO NUMERO 1 #########################
# salario = float(input("Qual é o salário do funcionário? "))
# porcentagem = (15/100) * salario
# aumento = (15/100 * salario) + salario if salario <= 1250 else (10/100 * salario) + salario
# salario = f"{salario:,.2f}".replace(',', ' ').replace('.', ',').replace(' ', '.')
# aumento = f"{aumento:,.2f}".replace(',', ' ').replace('.', ',').replace(' ', '.')

# print(f"\nQuem ganhava R${salario} passa a ganhar R${aumento}")


######################### VERSÃO NUMERO 2 #########################
# from locale import setlocale, currency, LC_ALL

# def formatar_numero(numero):
#     setlocale(LC_ALL, 'pt_BR.UTF-8')
#     return currency(numero, grouping=True, symbol='R$')

# salario = float(input("Qual é o salário do funcionário? "))
# porcentagem = (15/100) * salario
# aumento = (15/100 * salario) + salario if salario <= 1250 else (10/100 * salario) + salario

# print(f"\nQuem ganhava {formatar_numero(salario)} passa a ganhar {formatar_numero(aumento)}")


######################### VERSÃO NUMERO 3 #########################
def formatar_numero(numero):
    numero_formatado = f'R${numero:,.2f}'.replace(',', ' ').replace('.', ',').replace(' ', '.')
    return numero_formatado

salario = float(input("Qual é o salário do funcionário? "))
aumento = (15/100 * salario) + salario if salario <= 1250 else (10/100 * salario) + salario
print(f"\nQuem ganhava {formatar_numero(salario)} passa a ganhar {formatar_numero(aumento)}")
