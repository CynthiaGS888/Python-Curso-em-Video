#079.Valores_únicos_em_uma_Lista

resposta = " "
numeros = []

print("="*50)

while resposta not in "N":
    num = int(input("Digite um número: "))
    if num not in numeros:
        numeros.append(num)
        print("Valor adicionado.")
    
    else:
        print("Número repetido.")
        
    
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
        
print("="*50)
numeros.sort()
print(f"Os números colocados foram: {(numeros)}") 
   
print("="*50)