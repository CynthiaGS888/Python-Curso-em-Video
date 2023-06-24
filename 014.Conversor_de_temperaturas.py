#014.Conversor_de_temperaturas
from time import sleep
import colorama
colorama.init(autoreset=True)


print("="*50)
print(f"\033[31m{' Conversor de Temperaturas ':^50}")
print("="*50)

celsius = float(input("Digite a temperatura em Celsius: "))

sleep(1)
print("Convertendo . . . ")
sleep (1)

f = celsius * 1.8 + 32 

print(f"\033[35m{celsius}°\033[m em Fahrenheit dá: \033[35m{f}°")
print("="*50)