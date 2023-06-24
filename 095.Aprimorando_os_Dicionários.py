#095.Aprimorando_os_Dicionários
jogadores = list()
registro = dict()
gols = []
total = 0

print("="*50)
while True:
    registro.clear()
    registro["Nome"] = str(input("Qual o nome? "))
    Partidas = int(input(f"Quantas partidas {registro['Nome']} jogou? "))

    gols.clear()
    
    for vezes in range(0, Partidas):
        gol = int(input(f"Quantos gols fez na {vezes}ª partida? "))
        total += gol
        gols.append(gol)

    registro["Gols"] = gols[:]
    registro["Total"] = total
    
    jogadores.append(registro.copy())
    
    while True:
        resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if resposta not in "SN":
            print("Digite um  valor válido!")
        
        else:
            break
    
       
    if resposta == "N":
        break


print('='*50)

print("cod ", end="")
for i in registro.keys():
    print(f"{i:<15}", end='')

print()

print("-"*50)

for num, v in enumerate(jogadores):
    print(f'{num:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end="")
        
    print()

print("-"*50)

while True:
    busca = int(input("Qual jogador deseja saber mais [999 interrompe]? "))
    
    if busca == 999:
        break
    
    elif busca >= len(jogadores):
        print(f'Não existe jogador com o número {busca}!')
        
    else:
        print(f' --> Dados dos jogador {jogadores[busca]["Nome"]}')
        for i, g in enumerate(jogadores[busca]["Gols"]):
            print(f"    No jogo {i+1}, fez {g} gols!")
    
    print("-"*50)

print("Volte sempre! :D")