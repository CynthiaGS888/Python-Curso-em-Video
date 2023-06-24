#072.Número_por_extenso 
num = -1
continua = " "
contagem =  'zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'

print("~"*50)
while True:
    num = -1
    continua = " "
    while num < 0 or num > 20:
        num = int(input("Coloque um número entre 0 e 20: "))

    print(f"Parabéns, você digitou o número {contagem[num]}!")
    print("~"*50)
    
    while continua not in "NS":
        continua = str(input("Quer continuar [S/N]? ")).strip().upper()
        
    if continua == "N":
             break
        
print("~"*50)