#037.Convertendo_base_númericas
import colorama
colorama.init(autoreset=True)

def e():
    print("\033[31m="*50)

e()
num = int(input("Coloque um número para ser convertido: "))
e()
escolha = str(input("Quer converter em binário (1), octal (2) ou hexadecimal (3)? ")).lower()
e()


if escolha == "1":
    print(f"Seu número, {num}, convertido fica: {bin(num)[2:]}")
    e()

elif escolha == "2":
    print(f"Seu número, {num}, convertido fica: {oct(num)[2:]}")
    e()
    
elif escolha == "3":
    print(f"Seu número, {num}, convertido fica: {hex(num)[2:]}")
    e()
    
else:
    print("Coloque uma das letras propostas!")
    e()
    quit()