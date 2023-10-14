# from math import factorial
# num = int(input("Digite o número para o fatorial: "))
# print(f"O fatorial de {num} é {factorial(num)}")


num = int(input("Digite o número para o fatorial: "))
temp = num

for p in range(num, 1, -1):
    i = temp * (p-1)
    temp *= (p-1)
    
print(f"{num}! = {i}")



