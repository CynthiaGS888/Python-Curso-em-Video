#004.Dissecando_variável
import colorama
colorama.init(autoreset=True)


n = input("Escreva uma variável para ser avaliada: ")

print(f"\033[34mO seu tipo primitivo: {type(n).__name__}")
print(f"\033[34mÉ número? {n.isalnum()}")
print(f"\033[34mÉ decimal? {n.isdecimal()}")
print(f"\033[32mÉ número e letra? {n.isalnum()}")
print(f"\033[33mÉ letra? {n.isalpha()}")
print(f"\033[33mÉ só espaço? {n.isspace()}")
print(f"\033[33mÉ capitalizada primeira letra? {n.istitle()}")
print(f"\033[33mÉ só letras maiúsculas? {n.isupper()}")
print(f"\033[33mÉ só letras minúsculas? {n.islower()}")