#057.Validação_de_dados
 
sexo = ""
 
while sexo != "f" and sexo != "m":
     sexo = input("Qual o seu sexo biológico [F/M]? ").lower().strip()[0]
     if sexo != "f" and sexo != "m":
        print("Inválido. Digite algo entre [F/M].")
     
if sexo == "f":
    print("Perfeito, você é do sexo feminino.")
else:
    print("Perfeito, você é do sexo masculino.")