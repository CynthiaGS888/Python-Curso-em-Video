#081.Extraindo_dados_de_uma_Lista
numeros = []

while True:
    print("-"*50)
    n = int(input("Digite um valor: "))
    numeros.append(n)
    
    r = " "
    while not r in "SN":
        r = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
          
    if r == "N":
        break
    

print("-"*50)

print(f"Foram digitados {len(numeros)} números.")
print(" ")

numeros.sort(reverse=True)
print(f"Foi digitado, em ordem decrescente: {numeros}")
print(" ")

if 5 in numeros:
    print("O número 5 está na lista!")

else:
    print("O número 5 não está na lista!")


print("-"*50)

    
        
    