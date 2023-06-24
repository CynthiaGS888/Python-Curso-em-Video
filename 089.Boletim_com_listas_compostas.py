#89.Boletim_com_listas_compostas
'''ficha = []


while True:
    nome = str(input("Nome do aluno: "))
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    
    
    pergunta = " "
    while pergunta not in "SN":
        pergunta = str(input("Quer continuar? ")).strip().upper()[0]
    
    if pergunta == "N":
        break

print("-"*50)
print(f"{'BOLETIM GERAL':^50}")
print("-"*50)
print(f"{'No. Nome':<20} {'Média':>20}")
print("-"*50)


for no, aluno in enumerate(ficha):
    print(f"{no:<4} {aluno[0]:<10} {aluno[2]:>23.1f}")
    

while True:
    print("-"*50)
    pergunta = int(input("Quer ver a nota de qual aluno? (999 para): "))
    
    if pergunta == 999:
        print("Finalizando...")
        print("-"*50)
        break
    
    if pergunta <= len(ficha)-1:
        print(f"As notas de {ficha[pergunta][0]} são {ficha[pergunta][1]}")'''
        

ficha = []

while True:
    print("~"*50)
    nome = str(input("Digite o nome: "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    
    ficha.append([nome, [nota1, nota2], media])
    
    
    pergunta = " "
    
    while pergunta not in "SN":
        pergunta = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    
    if pergunta == "N":
        break


print(ficha)

print("~"*50)
print(f"{'BOLETIM GERAL':^50}")
print("~"*50)

print(f"{'No.':<12} {'Nome':<12} {'Média':^24}")

for num, aluno in enumerate(ficha):
    print(f"{num:<12} {aluno[0]:<12} {aluno[2]:^24}")

print("~"*50)

while True:
    pergunta = int(input("Deseja ver a nota de qual aluno? (999 interrompe): "))
    
    if pergunta == 999:
        print("Finalizando...")
        break
    
    elif pergunta <= len(ficha) - 1:
        print(f"As notas de {ficha[pergunta][0]} são {ficha[pergunta][1]}")
        print("~"*50)