#067.Tabuada_V3

def e():
    print("="*50)

num = 0

while True:
    e()
    num = int(input("Escolha um número para ver sua tabuada: "))
    e()
    if num >= 0:
        for c in range(1,11):
            print(f"{num} X {c} = {num*c}")
            c += 1
    elif num < 0:
        break
    
print("Programa encerrado. Até mais!")