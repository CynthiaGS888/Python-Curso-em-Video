#054.Grupo_da_maioridade

from datetime import date

hoje = date.today().year


nascs = []
maidade = 0
meidade = 0


for n in range(1,8):
    nasc = int(input(f"Coloque o {n}° ano de nascimento: "))
    nascs.append(nasc)
    
    for nasc in nascs:
        idade = hoje - nasc
    
    if idade >= 21:
        maidade += 1
    
    else:
        meidade +=1

print(f"A quantidade de maiores é: {maidade}\nE a quantidade de menores é: {meidade}")

