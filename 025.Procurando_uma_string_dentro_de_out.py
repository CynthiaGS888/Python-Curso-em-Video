#025.Procurando_uma_string_dentro_de_outra

import colorama
colorama.init(autoreset=True)
print("="*50)
nome = str(input("Digite seu nome: ")).lower()

nome = nome.split()

if "silva" in nome:
    print("\033[32mVocê tem Silva no nome. Legal :D")
    
else:
    print("\033[31mVocê não tem Silva no nome :/")

print("\033[33mMas provavelmente você já sabe disso...")
print("="*50)
