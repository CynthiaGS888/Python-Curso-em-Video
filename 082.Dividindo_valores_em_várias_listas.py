#082.Dividindo_valores_em_várias_listas

lista = []
pares = []
impares = []

print("="*50)

while True:
    num = int(input("Digite um número: "))
    
    lista.append(num)
    
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
        
    if resposta == "N":
        break

print(f"Os números digitados foram: {lista}")

for n in lista:
    if n % 2 == 0:
        pares.append(n)
        
    elif n % 2 != 0:
        impares.append(n)
        
print("="*50)
print(f"Os números pares são: {pares}")
print(f"Os números ímpares são: {impares}")
print("="*50)