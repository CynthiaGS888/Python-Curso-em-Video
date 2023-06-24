#070.Estatísticas_em_produtos
continua = " "
soma = mil = barato = cont = 0

print("-"*50)
print(f"{' Mercadinho Do Maurício ':-^50}")
print("-"*50)


while continua not in  "n":
    nome = str(input("Coloque o nome do produto: ")).strip().lower()
    preço = float(input("Coloque o preço do produto: R$"))
    cont += 1
    
    
    continua = " "
    while continua not in "sn":
        continua = str(input("Deseja continuar [S/N]? ")).strip().lower()[0]
        
    print("-"*50)
    soma += preço
    
    if preço >= 1000:
        mil += 1
    
    if cont == 1 or preço < barato:
       barato = preço 
       nomebarato = nome 
    
print(f"Todos os produtos custarão R${soma:.2f}")
print(f"{mil} produtos são acima de R$1.000.")
print(f"{nomebarato} é o produto mais barato, custando R${barato}.")
print("-"*50)