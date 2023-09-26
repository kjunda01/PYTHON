n1 = float(input("PRIMEIRA NOTA: "))
n2 = float(input("SEGUNDA NOTA: "))

print(f"Notas para média: {n1} e {n2}")
print("Fazendo a média...")
media = (n1 + n2) / 2

print(f"Média: {media} pontos.")
if media <= 5:
    print("Aluno REPROVADO!")
elif media <= 6.9:
    print("Aluno de RECUPERAÇÃO")
else:
    print("Aluno APROVADO!, parabéns!!")
