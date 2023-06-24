#077.Contando_vogais

palavras = 'arroz', 'feijao', 'macarrao', 'banana', 'maça', 'batata', 'tomate'

print("~"*50)

for palavra in palavras:
    vogais = ""
    cont = 0
    for letra in palavra:
        if letra.lower() in "aeiou":
            vogais += letra + " "
            cont += 1
        
        
    print(f"A palavra {palavra} tem de vogais: {vogais} \nTotalizando {cont} vogais.")
    print("~"*50)