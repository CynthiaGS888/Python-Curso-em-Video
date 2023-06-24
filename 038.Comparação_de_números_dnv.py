#038.Comparação_de_números_dnv
import colorama
colorama.init(autoreset=True)


num1 = float(input("Coloque o primeiro número: "))
num2 = float(input("Coloque o segundo número: "))

if num1 > num2:
    print(f"O primeiro valor: {num1}, é maior que o segundo: {num2}\nL\033[33mogo, o primeiro é o maior!")

elif num2 > num1:
    print(f"O segundo valor: {num2}, é maior que o primeiro: {num1}\n\033[33mLogo, o segundo é o maior!")

else:
    print("\033[33mOs valores são iguais!")