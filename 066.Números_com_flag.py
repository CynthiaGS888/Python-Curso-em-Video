#066.Números_com_flag

cont = 0
soma = 0 

while True:
    num = int(input("Coloque um número para somá-lo [999 para]: "))
    if num == 999:
        break 
    elif num != 999:
        cont += 1
        soma = soma + num
print(f"A soma de {cont} números, dá {soma}!")