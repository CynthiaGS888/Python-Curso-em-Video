#061.Progressão_aritmética_V2

'''num = int(input("Coloque o primeiro número para saber sua progressão aritmética: "))
r = int(input("Coloque a razão: "))
vzs1 = 0
vzs2 = 10

while vzs1 != vzs2:
    print(num, end=" \032 ")
    num += r
    vzs1 += 1
    
    if vzs1 == vzs2:
        resposta = input("Deseja ver mais termos, (S/N)? ").lower()
        
        if resposta == "s":
            vzs2 += int(input("Quantos termos deseja ver? "))
            continue
        
        else: 
            break
        
print("Acabou.")'''

primeiro = int(input("Digite o primeiro termo da P.A.: "))
razão = int(input("Digite a razão: "))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} \033", end=" ")
        termo += razão
        cont += 1  

    print("Pausa")
    mais = int(input("Quantos termos a mais? "))
    
print("Fim!")
print(f"{total} termos foram mostrados.")