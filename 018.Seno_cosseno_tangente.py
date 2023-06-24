#018.Seno_cosseno_tangente
from math import sin, cos, tan, radians
import colorama
colorama.init(autoreset=True)

def e():
    print("\033[33m-"*50)
    
e()
print(f"{' CALCULADORA DE SIN, COS E TAN ':-^50}")
e()

ang = float(input("Diga o ângulo que quer a conversão: "))

rad = radians(ang)

e()

print(f"O seno é: {sin(rad):.2f}.")
print(f"O cosseno é: {cos(rad):.2f}.")
print(f"A tangente é: {tan(rad):.2f}.")
e()