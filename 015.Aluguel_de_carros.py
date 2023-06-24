#015.Aluguel_de_carros

from time import sleep
import colorama
colorama.init(autoreset=True)

print("\033[33m="*50)

dias = int(input("Quantos dias foram alugados? "))
km = float(input("Quantos quilômetros foram usados? "))

print("\033[33m="*50)

aluguel = 60 * dias + 0.15 * km

sleep(1)
print("Calculando.", end='')
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".")
sleep(1)
print("\033[33m="*50)
print(f"O total à pagar é de R${aluguel}")
print("\033[33m="*50)