#022.Analisador_de_textos
import colorama
colorama.init(autoreset=True)

print("-="*50)
nome = str(input("Digite seu nome completo: "))
print("-="*50)

print(f"Em letras maiúsculas: \033[31m{nome.upper()}")
print(f"Em letras minúsculas: \033[31m{nome.lower()}")
nome_s = nome.replace(" ","")
print(f"O nome possui\033[31m {len(nome_s)}\033[m letras.")
print(f"O primeiro nome possui \033[31m{len(nome.split()[0])}\033[m letras.")

print("-="*50)