#85.Listas_com_pares_e_ímpares

lista = [[],[]]


for c in range(1,8):
    numeros = int(input(f"Digite o {c}° número: "))
    if numeros % 2 == 0:
        lista[0].append(numeros)
        
    elif numeros % 2 != 0:
        lista[1].append(numeros)
        
lista[0].sort()
lista[1].sort()

print("~"*50)
print(f"Pares: {lista[0]}\nImpares: {lista[1]}")
print("~"*50)