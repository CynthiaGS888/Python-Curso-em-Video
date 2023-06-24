#056.Analisador_completo
def e():
    print("="*30)
    
    
soma = 0
quant = 0
maioridade = 0
nomemaisvelho = ""

e()
for p in range(1, 5):
    nome = str(input(f"Coloque o {p}° nome: ")).lower().strip()
    idade = int(input(f"Coloque a {p}° idade: "))
    sexo = str(input(f"Coloque o {p}° sexo: ")).lower().strip()
    e()
    
    soma += idade
    média = soma / 4
    
    if (sexo == "feminino" or "f") and idade < 20:
        quant += 1
    
    if p == 1 and (sexo in "mM" or sexo == "masculino"):
        maioridade = idade
        nomemaisvelho = nome 
    if sexo in "Mm" and idade > maioridade:
        maioridade = idade
        nomemaisvelho = nome
    
print(f"A média de idade é de {média:.2f} anos.")
print(f"Há {quant} mulheres menores de idade.")
print(f"O homem mais velho tem {maioridade} anos e seu nome é {nomemaisvelho}.")
