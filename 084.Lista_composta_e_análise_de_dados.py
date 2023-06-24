#84.Lista_composta_e_análise_de_dados

dados = []
individual = []
maior = menor = 0

print("~"*50)
while True:
    individual.append(str(input("Digite o nome: ")))
    individual.append(float(input("Digite o peso: ")))
    
    if len(dados) == 0:
        maior = menor = individual[1]
    
    else:
        if individual[1] > maior:
            maior = individual[1]
            
        if individual[1] < menor:
            menor = individual[1]
    
    dados.append(individual[:])
    individual.clear()
        
    
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    print("~"*50)
    
    if resposta == "N":
        break

print(f"Foram cadastradas {len(dados)} pessoas!")
print(f"O maior peso ({maior}Kg) foi de: ", end="")

for p in dados:
    if p[1] == maior:
        print(f"{p[0]}", end=" ")
        
print(" ")

print(f"O menor peso ({menor}kg) foi de: ", end="")

for p in dados:
    if p[1] == menor:
        print(f"{p[0]}", end=" ")

print(" ")