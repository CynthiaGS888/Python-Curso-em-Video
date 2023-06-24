#033.Maior_e_menor_valores

import colorama
colorama.init(autoreset=True)

print("="*50)
numeros = float(input("Coloque o primeiro valor: ")), float(input("Coloque o segundo valor: ")), float(input("Coloque o terceiro valor: "))
print("="*50)
print(f"\033[33mO maior número digitado foi \033[35m{max(numeros)}\033[33m.")
print(f"\033[33mO menor número digitado foi \033[35m{min(numeros)}\033[33m.")
print("="*50)