#092.Cadastro_de_Trabalhador_em_Python

from datetime import date

cadastro = dict()

print("="*50)
# 1- Ler nome, ano de nascimento e carteira de trabalho
# 2- Cadastrar nome e carteira de trabalho
# 3- Calcular e cadastrar a idade no dicionário
cadastro["Nome"] = str(input("Nome completo: "))
nascimento = int(input("Ano de nascimento: "))
anoatual = date.today().year
idade = anoatual - nascimento
cadastro["Idade"] = idade
cadastro["CTPS"] = int(input("Carteira de trabalho ('0' se não tem): "))

# 4- Checar se a ctps é != de 0 e...
# 5- Cadastrar no dicionário ano de contratação e salário 
# 6- Calcular com quantos anos vai se aposentar (35  anos de colaboração) e cadastrar
if cadastro["CTPS"] != 0:
    contratação = int(input('Ano de contratação: '))
    cadastro["Contratação"] = contratação
    cadastro['Salário'] = float(input('Salário: R$'))
    
    aposentadoria = (35 - (anoatual - contratação)) + idade
    cadastro['Aposentadoria'] = aposentadoria

print("="*50)

for k,v in cadastro.items():
    print(f"{k} = {v}")

print("="*50)
print(cadastro)