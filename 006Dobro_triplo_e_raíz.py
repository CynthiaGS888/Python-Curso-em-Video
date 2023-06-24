import colorama
from math import sqrt, pow
from time import sleep
colorama.init(autoreset=True)


def e():
    print("\033[33m="*50)
    
e()
print(f"\033[31m{' Mini Calculadora ':=^50}")
e()
sleep(1)
num = float(input("Me diga um valor: "))
e()
sleep(1)
print(f"Dobro: {num*2}")
print(f"Triplo: {num*3}")
print(f"Quádruplo: {num*4}")
print(f"Quíntuplo: {num*5}")
print("\033[33m-"*50)
print(f"Raíz quadrada: {sqrt(num):.1f}")
print(f"Sobre dois: {pow(num, 2)}")

e()
