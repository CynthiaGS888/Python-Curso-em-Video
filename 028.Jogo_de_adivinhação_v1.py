#028.Jogo_de_adivinhação_v1
from time import sleep
from random import randint
import colorama
colorama.init(autoreset=True)

chute = -1

print("="*50)
print(f"{' NÃO ADIVINHARÁ O NÚMERO ':^50}")
print("="*50)
print(f'{"Pensei num número entre 0 e 5. Tente adivinhar!":^50}')
print(" ")

num = randint(0,5)


while chute > 5 or chute < 0:
    chute = int(input("Adivinhe o número: "))

print("="*50)
print("Analisando",end="")
sleep(1)
print(".",end="")
sleep(1)
print(".",end="")
sleep(1)
print(".")
print("="*50)

print(f"Você chutou:{chute}\nO computador pensou em: {num}")

if chute == num:
    print("\033[32mVocê acertou, parabéns!")
    
else:
    print("\033[31mVocê errou ;-;")
    
print("="*50)