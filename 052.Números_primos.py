#052.Números_primos
import colorama
colorama.init(autoreset=False)

print("=" * 30)
print("Descubra se é um número primo!")
print("=" * 30)

num = int(input("Coloque um número inteiro: "))


c = 0

print("É divisível por: ", end="")

for n in range(1,num+1):
    if num % n == 0:
        print(n, end=" ")
        c += 1

print("") #Espaço pro end=""

if c > 2:
    print(f"{num} não é primo.")

else: print(f"{num} é primo.")


print("=" * 30)
print("Correção")
print("=" * 30)

num2 = int(input("Coloque um número: "))
tot = 0

for c in range(1,num2 + 1):
    if num2 % c == 0:
        print("\033[33m", end=" ")
        tot += 1
    
    else:
        print("\033[31m", end=" ")
    print(c, end="")

print(f"\n\033[mO número foi divisível {tot} vezes.")

if tot == 2:
    print("Por isso ele é PRIMO!.")

else: 
    print("Por isso ele NÃO é primo!")