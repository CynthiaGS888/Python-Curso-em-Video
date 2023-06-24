#87.Mais_sobre_Matriz_em_Python

soma = terceira = maior = 0
lista = [[], [], []]

for c in range(1,10):
    num = int(input("Digite um número: "))
    
    if num % 2 == 0:
        soma += num
    
    if c <= 3:
        lista[0].append(num)
    
    elif c > 3 and c <= 6:
        lista[1].append(num)
        
    elif c > 6 and c <= 9:
        lista[2].append(num)

print(f"Lista: {lista}")

print("-"*50)
print(f"[{lista[0][0]:^8}] [{lista[0][1]:^8}] [{lista[0][2]:^8}]")
print(f"[{lista[1][0]:^8}] [{lista[1][1]:^8}] [{lista[1][2]:^8}]")
print(f"[{lista[2][0]:^8}] [{lista[2][1]:^8}] [{lista[2][2]:^8}]")
print("-"*50)

print(f"A soma dos pares dá {soma}.")

terceira = lista[0][2] + lista [1][2] + lista[2][2]

print(f"A soma da terceira coluna é {terceira}.")

maior = max(lista[1])  

print(f"O maior número da segunda linha é {maior}.")
print("-"*50)