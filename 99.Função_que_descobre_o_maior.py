#99.Função_que_descobre_o_maior

from time import sleep

def maior(*num):
    
    if len(num) == 0:
        print('Nenum valor foi colocado.')
    
    elif len(num) > 0:
    
        for i, n in enumerate(num):
            if i == 0:
                mai = n
                
            elif i > 0 and n > mai:
                mai = n 
        
        print('~' * 50)
        
        print('Analisando os números...')
        sleep(1) 
                
        print(f'Foram analisados ', end="")
        for n in num:
            print(n, end=' ', flush=True)
            sleep(0.5) 
        print(f'no total {len(num)} números.')    
        
        print(f'O maior número é {mai}.')
    
    print('~' * 50)


maior(5, 7, 2, 9, 1)

maior(4, 6, 3)

maior(2, 4)

maior()