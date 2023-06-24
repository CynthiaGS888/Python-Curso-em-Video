#059.Menu_de_opções
from time import sleep

def e():
    print("="*50)
    
maior = 0
operação = 0    

e()
num1 = float(input("Coloque o primeiro valor: "))
num2 = float(input("Coloque o segundo valor: "))

    
while operação != 5:
    e()
    sleep(1)
    print('''Selecione a operação lógica: 
    [1] Somar
    [2] Multiplicar 
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    e()
    operação = int(input("Qual opção? "))

    if operação == 1:
        conta = num1 + num2 
        print(f"A soma entre {num1} e {num2} dá {conta}.")
        e()
        
        
    elif operação == 2:
        conta = num1 * num2
        print(f"A multiplicação entre {num1} e {num2} dá {conta}")
        e()
        
    
    elif operação == 3:
        if num2 > num1:
            maior = num2
            print(f"O {maior} é maior que o {num1}.")
            
        
        else: 
            maior = num1
            print(f"O {maior} é maior que o {num2}.")
            
    
    elif operação == 4:
        num1 = float(input("Coloque o primeiro valor: "))
        num2 = float(input("Coloque o segundo valor: "))
        e()
    
    elif operação == 5:
        print("Finalizando...")
        sleep(1)
    
    else:
        print("Coloque um valor válido entre 1 e 5.")
        
print("Fim de programa. Volte sempre!")