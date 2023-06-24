#024.Verificando_as_primeiras_letras

import colorama
colorama.init(autoreset=True)

cidade = str(input("Digite o nome de uma cidade: ")).lower()

print(f"A cidade começa com Santo?", end=" ")

if 'santo' in cidade:
    print("\033[32mSim, começa com Santo.")

else:
    print("\033[31mNão, não começa com Santo :/")