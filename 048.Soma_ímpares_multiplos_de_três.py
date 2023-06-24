#048.Soma_ímpares_multiplos_de_três
soma = 0
cont = 0
for n in range(1,501,2):
    if n % 3 == 0:
        cont += 1
        soma += n

print(f"A soma de todos múltiplos de 3, impares, entre 1 e 500 é: {soma}\nForam {cont} valores solicitados!")