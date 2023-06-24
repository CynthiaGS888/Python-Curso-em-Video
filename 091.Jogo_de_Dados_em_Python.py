#091.Jogo_de_Dados_em_Python

from random import randint
from operator import itemgetter
from time import sleep

print(f"{'> JOGANDO O DADO <':-^50}")

Jogadas = dict()

j1 = randint(1,6)
j2 = randint(1,6)
j3 = randint(1,6)
j4 = randint(1,6)

jogadas = {'Primeiro jogador': j1,
           'Segundo jogador': j2,
           'Terceiro jogador': j3,
           'Quarto jogador': j4}

for k, v in jogadas.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)


jogadasSorted = sorted(jogadas.items(), key=itemgetter(1), reverse=True)


print(f"{'> RANKING DOS JOGADORES <':-^50}")

for n, v in enumerate(jogadasSorted):
    print(f"Em {n+1}° lugar ficou o {v[0]} com {v[1]}")
    sleep(0.5)

print('-'*50)