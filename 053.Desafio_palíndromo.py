#053.Desafio_palíndromo

frase = str(input("Digite a frase: ")).strip().lower() #O strip tirou os espaços antes e depois
palavras = frase.split()  #Separa as palavras numa lista
junto = "".join(palavras) #junta tudo juntinho

inverso = "" #Vazio por enquanto

for letras in range(len(junto) - 1, -1, -1): #Faz a frase ficar ao contrário
    inverso += junto[letras] # ????????
    
if inverso == junto:
    print("Temos um palíndromo!")

else: 
    print("A frase digitada não é um palíndromo.")
    
#--------------------------------------------------------------------
print("="*30)
inverso2 = junto[::-1]
print(inverso2)

if inverso2 == junto:
    print("Temos um palíndromo!")

else: 
    print("A frase digitada não é um palíndromo.")