#019.Sorteando_um_item_da_lista
import random
from time import sleep
import colorama
colorama.init(autoreset=True)

print("~"*50)
alunos = [(input("Coloque o nome do primeiro aluno: ")),
        (input("Coloque o nome do segundo aluno: ")),
        (input("Coloque o nome do terceiro aluno: ")),
        (input("Coloque o nome do quarto aluno: "))]

print("~"*50)
print(f"Os alunos escritos são: {alunos}")
print("~"*50)
print("\033[33mSorteando", end="")
sleep(1)
print("\033[33m.",end="")
sleep(1)
print("\033[33m.",end="")
sleep(1)
print("\033[33m.")
sleep(1)
print("~"*50)

print(f"\033[31m{ 'O aluno escolhido é:' :^50}")
sorteado = random.choice(alunos)
sleep(1)
print(f"\033[32m{sorteado:^50}")
print("~"*50)