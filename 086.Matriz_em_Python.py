#86.Matriz_em_Python

'''lista = [[],[],[]]

'for c in range (1,10):
    num = int(input("Digite um número: "))
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
print("-"*50)'''

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(3):
    for coluna in range(3):
        lista[linha][coluna] = int(input(f"Digite um número para matriz [{linha+1}, {coluna+1}]: ")) 


for l in range(3):
    for c in range(3):
        print(f"[{lista[l][c]:^8}]", end=" ")
    print(" ")