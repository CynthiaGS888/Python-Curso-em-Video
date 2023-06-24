#047.Contagem_em_pares
print("Números pares de 1 à 50: ")
for c in range(2,51,2):
    print(c, end=" ")
    
print(" ")
print("="*50)
print("OU")
print("="*50)

for n in range(2,51):
    if n % 2 == 0:
        print(n, end=" ")
