#039.Alistamento_militar
from datetime import date

nasc = int(input("Informe seu ano de nascimento: "))
gênero = str(input("Informe seu gênero de nascimento (M ou F): ")).lower()

ano = date.today().year

id = ano - nasc



if id < 18 and gênero == "m":
    idade = 18 - id
    print(f"Muito novo para se alistar. Você tem {id} anos, ainda faltam {idade} anos para poder se alistar ({ano + idade}).")
    
elif id > 18 and gênero == "m":
    idade = id - 18
    print(f"Já passou da idade de se alistar. Você tem {id} anos e deve ter se alistado em {ano - idade}.")
    
elif id == 18 and gênero == "m": 
    print("Você está na idade de se alistar!")

elif gênero == "f":
    print("Devido ao seu sexo biológico, você não precisa se alistar.")