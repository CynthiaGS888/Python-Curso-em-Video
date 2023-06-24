#030.Par_ou_Ímpar
from time import sleep
import colorama
colorama.init(autoreset=True)

print("\033[35m~"*50)
print(f"{' PAR OU IMPAR ':^50}")
print("\033[35m~"*50)

print(" ")

num = int(input("Digite um número: "))

print(" ")

print("Analisando...")
print(" ")

sleep(2)

print("\033[35m~"*50)

print("Analisado, o resultado é: ")

if num % 2 == 0:
    print("\033[33mO número é \033[31mpar\033[33m!")
    
else:
    print("\033[33mO número é \033[31mímpar\033[33m!")

print("\033[35m~"*50)
