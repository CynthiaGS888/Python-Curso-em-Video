#017.Catetos_e_hipotenusa

import colorama
colorama.init(autoreset=True)
from math import hypot

print("~"*50)
print(f"\033[36m{' Calculadora de Hipotenusa ':^50}")
print("~"*50)

ca = float(input("Coloque o primeiro cateto: "))
co = float(input("Coloque o segundo cateto: "))
print("~"*50)

hip = hypot(ca,co)

print(f"A hipotenusa de \033[36m{ca}\033[m com \033[36m{co}\033[m é: \033[36m{hip:.1f}\033[m.")
print("~"*50)