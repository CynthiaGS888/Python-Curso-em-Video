#069.Análise_de_dados_em_grupo

def e():
    print("="*50)


idade = 0
pontidade = pontmenina = ponthomem = 0
continua = " "

e()
print(f"{' CADASTRE UMA PESSOA ':=^50}")
e()

while continua != "n":
    
    idade = int(input("Coloque a idade: "))
    sexo = " "
    while sexo not in "fm":
        sexo = str(input("Coloque o sexo [F/M]: ")).strip().lower()[0]
   
    e()
    continua = " "
    while continua not in "sn":
        continua = str(input("Quer continuar [S/N]? " )).strip().lower()[0]
    e()
    if idade >= 18:
        pontidade += 1
        
    elif idade < 20 and sexo in "fF":
        pontmenina += 1
     
    elif sexo in "mM":
        ponthomem += 1
     
print(f"A quantidade de pessoas na maioridade são: {pontidade}.\nA quantidade de meninas menores de 20 são: {pontmenina}\nA quantidade de homens são: {ponthomem}")   
e()

