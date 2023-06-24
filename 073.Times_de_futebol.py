#073.Times_de_futebol

times = 'América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Red bull bragantino', 'Santos', 'São paulo', 'Vasco'
def e():
    print("="*110)
    
e()

print("Os times são: ", end="")
for time in times:
    print(time, end=" ")
print("")
    
e()

print(f"Os cinco primeiros colocados são: {times[0:5]}")

e()

print(f"Os quatro últimos colocados são: {times[-4:]}")

e()

print(f"Organizados em ordem alfabética: {sorted(times)}")

e()

print(f"O flamengo está na {times.index('Flamengo')+1}° posição.")

e()