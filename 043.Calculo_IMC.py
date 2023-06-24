#043.Calculo_IMC

import math

print("=" * 50)
print("Irei calcular seu IMC!")
print("=" * 50)

peso = float(input("Coloque seu peso: "))
altura = float(input("Coloque sua altura: "))
print("=" * 50)

imc = peso / altura**2
imc = round(imc, 1)


print(f"Seu IMC é: {imc}")

if imc < 18.5:
    print("Você está abaixo do peso ideal.")
    print("=" * 50)

elif 18.5 <= imc < 25:
    print("Você está no seu peso ideial!")
    print("=" * 50)

elif 25 <= imc < 30:
    print("Você está no sobrepeso.")
    print("=" * 50)

elif 30 <= imc < 40:
    print("Você está na obesidade.")
    print("=" * 50)

else: 
    print("Você está na obesidade mórbida.")
    print("=" * 50)

