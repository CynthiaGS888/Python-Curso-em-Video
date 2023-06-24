#100.Funções_para_sortear_e_somar

from random import randint
from time import sleep

def esc(texto):
    tamanho = len(texto) + 2
    print('='* tamanho)
    print(f' {texto}')
    print('='* tamanho)

esc("Sorteador de números")

def sorteia(lista):
    for contador in range(0, 5):
        lista.append(randint(1, 10))
        
    print("Sorteando números: ", end='')
    for n in lista:
        print(n, end=' ', flush=True)
        sleep(0.3)
    print(f'no total 5 números!')
    
    print('-' * 50)
 
 
 
def somapar(lista):
    print(f'Dos números: {lista}, os pares são: ')
    
    soma = 0
    for n in lista:
         print(n, end=' ')
         
         if n % 2 == 0:
             soma += n
    
    print(f'e a soma dos números pares dá: {soma}')
    print('-' * 50)
            
     
     

teste = []
sorteia(teste)

esc('Somando os pares')

somapar(teste)