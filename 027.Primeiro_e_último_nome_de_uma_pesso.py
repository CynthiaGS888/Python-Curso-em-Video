#027.Primeiro_e_último_nome_de_uma_pessoa

import colorama
colorama.init(autoreset=True)

print("\033[35m="*50)

nome = str(input("Digite seu nome completo: "))

nome = nome.split()

print(f"Seu primeiro nome é '\033[31m{nome[0]}\033[m' e seu útimo é '\033[31m{nome[-1]}\033[m'.")

print("\033[35m="*50)

