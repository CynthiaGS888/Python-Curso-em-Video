#020.Sorteando_ordem_na_lista

import random
from time import sleep
import colorama
colorama.init(autoreset=True)

print("\033[36m=-"*25)
alunos = [(input("Primeiro aluno: ")), (input("Segundo aluno: ")),
          (input("Terceiro aluno: ")), (input("Quarto aluno: "))]
print("\033[36m=-"*25)

print("\033[33mSorteando a ordem", end="")
sleep(1)
print('\033[33m.',end='')
sleep(1)
print('\033[33m.',end='')
sleep(1)
print('\033[33m.')
sleep(1)
print("\033[36m=-"*25)

random.shuffle(alunos)

print(f"A ordem da apresentação será: {alunos}")
print("\033[36m=-"*25)