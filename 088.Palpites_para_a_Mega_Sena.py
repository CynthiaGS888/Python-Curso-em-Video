#88.Palpites_para_a_Mega_Sena

from random import randint
from time import sleep

lista = []
jogos = []

print("="*50)
print(f"{'MEGA SENA':^50}")
print("="*50)

vezes = int(input("Quantas vezes quer que eu sorteie? "))
print(" ")
print(f"{' carregando ':=^50}")
print(" ")
sleep(2)
for times in range(vezes):
    for c in range(0,6):
        
        n = randint(1,60)
        
        if n not in lista:
            lista.append(n)
        
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

for l, c in enumerate(jogos):
    print(f"{l+1}° jogo: {c}")
    sleep(1)

print("="*50)

