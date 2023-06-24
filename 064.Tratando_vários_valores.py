#64.Tratando_vários_valores

quant = 0
soma = 0
num  = 0

while num != 999:
    print("Digite um número inteiro ou 999 para parar.")
    num = int(input("Coloque um número inteiro: "))
    
    if num != 999:
        quant += 1
        soma += num    
        
print(f"Foram somados {quant} números, dando {soma}.")