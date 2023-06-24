#034.Aumentos_múltiplos

import colorama
colorama.init(autoreset=True)
print("~"*50)
salario = float(input("Qual o seu salário? R$"))

print("~"*50)

if salario <= 1250:
    salario = salario + (salario * 0.15)
    print(f"\033[33mVocê ganhou um aumento de \033[32m15% \033[33mtotalizando \033[32mR${salario:.2f}\033[33m.")

else:
    salario = salario + (salario * 0.10)
    print(f"\033[33mVocê ganhou um aumento de \033[32m10% \033[33mtotalizando \033[32mR${salario:.2f}\033[33m.")
    

print("~"*50)