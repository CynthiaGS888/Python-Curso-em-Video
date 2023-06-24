#058.Jogo_adivinhação_V2

from random import randint

def e():
    print("="*50)
    
numale = randint(1, 10)
chute = 1
tentativas = 0

    
e()
print(f"{' JOGO DE ADVINHAÇÃO ':=^50}")
e()

while chute != numale:
    chute = int(input("Faça seu chute aqui: "))
    tentativas += 1
    
    
    if chute > numale:
        print("Muito alto :/")
        e()
    
    elif chute < numale:
        print("Muito baixo :/")
        e()
    
print(f"Parabéns! Acertou do pc! Foram em {tentativas} tentativas!")
e()