pri_num = int(input("Primeiro número: "))
sec_num = int(input("Segundo número: "))

if pri_num > sec_num:
    print(f"{pri_num} é maior que {sec_num}")
elif sec_num > pri_num:
    print(f"{sec_num} é maior que {pri_num}")
else:
    print(f"{pri_num} e {sec_num} são iguais.")
    