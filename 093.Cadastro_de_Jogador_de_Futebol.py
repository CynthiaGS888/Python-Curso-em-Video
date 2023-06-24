#093.Cadastro_de_Jogador_de_Futebol

registro = dict()
gols = []
total = 0

print("="*50)

registro["Nome"] = str(input("Qual o nome? "))
Partidas = int(input(f"Quantas partidas {registro['Nome']} jogou? "))

for vezes in range(0, Partidas):
    gol = int(input(f"Quantos gols fez na {vezes}ª partida? "))
    total += gol
    gols.append(gol)

registro["Gols"] = gols[:]
registro["Total"] = total

print("="*50)

print(registro)

print("="*50)

for k,v in registro.items():
    print(f"{k} -----> {v}")

print("="*50)

print(f"O jogador {registro['Nome']} participou de {Partidas} partidas!")

for n, item in enumerate(registro["Gols"]):
    print(f" -> Na partida {n+1}, ele fez {item} gols.")

print(f"No total foram {registro['Total']} gols!")