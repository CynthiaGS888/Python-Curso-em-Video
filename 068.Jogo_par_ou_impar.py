#068.Jogo_par_ou_impar

from random import randint

def e():
    print("="*50)

vence = 0 
poui = " "
 
while True:
    num_comp = randint(0,10)
    e()
    num_pess = int(input("Diga um valor: ")) 

    poui = str(input("Quer par ou impar [P/I]? ")).strip().lower()[0]
    e()

    conta = num_comp + num_pess
    
    print(f"Você jogou {num_pess} e o pc jogou {num_comp}, dando {conta}")
    print("Deu par" if conta % 2 == 0 else "Deu impar")
    
    if poui == "p":
        if conta % 2 == 0:
            print("Parabéns, você venceu")
            vence += 1
            
        
        else: 
            print("Você perdeu :/")
            break
        
    if poui == "i":
        if conta % 2 == 1:
            print("Parabéns, você venceu")
            vence += 1
            
        
        else: 
            print("Você perdeu :/")
            break

print(f"Você venceu {vence} vezes!")
    
    
"""
    if conta % 2 == 0 and poui == "p":
        vence +=1
        print(f"Você chutou {num_pess}\nO pc chutou: {num_comp}\nFoi par.")
        print("Parabéns você venceu.")
        e()
        continue
    
    elif conta % 2 != 0 and poui == "i":
        vence += 1
        print(f"Você chutou {num_pess}\nO pc chutou: {num_comp}\nFoi impar.")
        print("Parabéns você venceu.")
        e()
        continue
        
    elif conta % 2 == 0 and poui == "i":
        print(f"Você chutou: {num_pess}\nO pc chutou: {num_comp}\nFoi impar.")
        print(f"Que pena, errou. Você ganhou {vence} vezes!")
        e()
        break
    
    elif conta % 2 != 0 and poui == "p":
        print(f"Você chutou: {num_pess}\nO pc chutou: {num_comp}\nFoi par.")
        print(f"Que pena, errou. Você ganhou {vence} vezes!")
        e()
        break"""
        

            