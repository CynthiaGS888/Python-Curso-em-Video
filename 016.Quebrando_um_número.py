#016.Quebrando_um_número
from time import sleep
import colorama
colorama.init(autoreset=True)

print("="*50)
num = float(input("Me diga um número real: "))
print(" ")
print(f"\033[33m{' Processando... ':^50}")
print(" ")
print(f"A parte inteira do número {num} é \033[32m{num:.0f}\033[m.")
print("="*50)