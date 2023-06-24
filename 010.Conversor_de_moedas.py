#010.Conversor_de_moedas

from time import sleep
import colorama
colorama.init(autoreset=True)

reais = float(input("Quantos reais possui na carteira? R$"))

dol = reais / 5.07
print("~~~~~~~~~~~~~~~~")
print("Convertendo...")
sleep(1)
print("~~~~~~~~~~~~~~~~")

print(f"R${reais} em dólares atualmente está \033[32mUS${dol:.2f}.")