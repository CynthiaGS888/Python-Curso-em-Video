#045.Jokenpo

import random
import colorama
from time import sleep
colorama.init(autoreset=True)

def e():
    print("\033[36m="*40)

print(f"\033[36m{' JOKENPÔ ':=^40}")


num = random.randint(1,3) # 1= pedra / 2= papel / 3= tesoura

chute = str(input("Faça seu chute, pedra, papel ou tesoura: ")).lower()

e()
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
e()


if (num == 1 and chute == "pedra") or (num == 2 and chute == "papel") or (num == 3 and chute == "tesoura"):
    print("\033[33mEmpatou! Jogue novamente!")
    e()
    
elif (num == 1 and chute == "papel") or (num == 2 and chute == "tesoura") or (num == 3 and chute == "pedra"):
    print("\033[032mVocê ganhou! Parabéns!")
    e()
    
elif (num == 1 and chute == "tesoura") or (num == 2 and chute == "pedra") or (num == 3 and chute == "papel"):
    print("\033[031mVocê perdeu :/")
    e()

else:
    print("Valor inválido! Tente novamente.")