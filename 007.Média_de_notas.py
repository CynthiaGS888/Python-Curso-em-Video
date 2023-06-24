#007.Média_de_notas
import colorama
from time import sleep
colorama.init(autoreset=True)

print(f"\033[32m{' Calculadora de Média ':~^50}")

nota1 = float(input("Coloque a primeira nota: "))
nota2 = float(input("Coloque a segunda nota: "))

print("\033[36m-"*50)
sleep(1)
print("Calculando...")
sleep(1)
print("\033[36m-"*50)
print(f"Com as notas {nota1} e {nota2}, sua média é {(nota1 + nota2)/2:.1f}")
print("\033[32m~"*50)