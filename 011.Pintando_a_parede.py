#011.Pintando_a_parede
from time import sleep
import colorama
colorama.init(autoreset=True)

print(f"\033[31m{'  Pintando a Parede ':-^50}")

largura = float(input("Coloque a largura em metros: "))
altura = float(input("Coloque a altura em metros: "))

print(f"\033[31m-"*50)

print("Calculando área. . . ")
print(f"\033[31m-"*50)
sleep(1)
area = largura*altura
print(f"{largura} vezes {altura} dá {area:.0f}m².")
print(f"Você precisará de \033[33m{area/2:.1f} litros de tinta \033[mpara pintar a parede.")
print(f"\033[31m-"*50)
