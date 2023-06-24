#003.Soma_entre_números
from time import sleep
import colorama
colorama.init(autoreset=True)

print(f"{' Soma de dois números ':-^50}")

num1 = float(input("Coloque o primeiro número: "))
num2 = float(input("coloque o segundo número: "))

print("-" * 50)

print(f"A soma entre {num1} e {num2} é:")
sleep(1)
print("\033[33mSomando...")
sleep(1)
print(f"\033[32m{num1 + num2}!")