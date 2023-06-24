#050.Soma_dos_pares
soma = 0
cont = 0

for c in range(1,7):
    n1 = int(input("Coloque um número: "))
    if n1 % 2 == 0:
        cont += 1
        soma += n1

print(f"Foram {cont} valores somados, totalizando {soma}.")