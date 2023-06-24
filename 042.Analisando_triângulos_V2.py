#042.Analisando_triângulos_V2

r1 = float(input("Coloque a primeira reta: "))
r2 = float(input("Coloque a segunda reta: "))
r3 = float(input("Coloque a terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("É possível formar um triângulo! ", end="")
    
    if r1 == r2 == r3:
        print("O triângulo é equilátero!")
    
    elif r1 != r2 != r3 and r1 != r3:
        print("O triângulo é escaleno!")
    
    else:
        print("O triângulo é isósceles!")
    
    
else:
    print("Não é possível formar um triângulo :/")