#026.Primeira_e_última_ocorrência_de__uma_ string
import colorama
colorama.init(autoreset=True)

print("-"*50)
frase = str(input("Digite uma frase: ")).lower().strip()
print("-"*50)

print(f"'A' aparece \033[31m{frase.count('a')} \033[mvezes.")

print(f"O primeiro 'A' aparece na \033[31m{frase.find('a')+1}ª\033[m posição")
print(f"O último 'A' aparece na \033[31m{frase.rfind('a')+1}ª\033[m posição")
print("-"*50)