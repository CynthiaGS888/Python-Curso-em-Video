#041.Categoria_natação
from datetime import date

ano = date.today().year

nasc = int(input("Coloque seu ano de nascimento: "))

idade = ano - nasc

print(f"Você tem {idade} anos.")

if idade <= 9:
    print("Você está na categoria MIRIM.")
    
elif  9 < idade <= 14:
    print("Você está na categoria INFANTIL.")
    
elif 14 < idade <= 19:
    print("Você está na categoria JÚNIOR.")

elif 19 < idade <= 25:
    print("Você está na categoria SÊNIOR.")

elif idade > 25:
    print("Você está na categoria MASTER.")