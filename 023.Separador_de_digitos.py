#023.Separador_de_digitos
import colorama
colorama.init(autoreset=True)

num = 0

print("~"*50)
num = str(input("Coloque um número entre 0 e 9999: "))

print(f"\033[36mMilhar: {num[0]}")
print(f"\033[36mCentena: {num[1]}")
print(f"\033[36mDezena: {num[2]}")
print(f"\033[36mUnidade: {num[3]}")
print("~"*50)