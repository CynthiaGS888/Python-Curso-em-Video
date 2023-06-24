#98.Função_de_Contador
from time import sleep


def contador(início, fim, passo):    
    print('='* 50)

    print(f'Início: {início} \nFim: {fim} \nPasso: {passo}')
    sleep(2)
    
    print('-'*50)
    
    cont = início
    if passo > 0:
        while cont <= fim:
            print(cont, end=" - ", flush=True)
            sleep(0.5)
            cont += passo
        
        print("FIM")
        
    elif passo < 0:
        while cont >= fim:
            print(cont, end=' - ', flush=True)
            sleep(0.5)
            cont += passo
        
        print("FIM") 
    
    elif passo == 0:
        passo =+ 1
        while cont <= fim:
            print(cont, end=" ", flush=True)
            sleep(0.5)
            cont += passo
            
        print("FIM")
    
    print('='* 50)
    
    
contador(1, 10, 1)
contador(10, 0, -2)

i = int(input("Digite o número inicial: "))
f = int(input("Digite o número final: "))
p = int(input('Digite de quanto em quanto a contagem: '))
contador(i, f, p)
