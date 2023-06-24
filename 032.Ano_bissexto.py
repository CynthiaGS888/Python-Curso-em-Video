#032.Ano_bissexto

import colorama
colorama.init(autoreset=True)

def e():
    print("\033[35m="*50)
    
e()
print(f"{' ANO BISSEXTO ':=^50}")
e()

print(" ")

ano = int(input("Digite o ano que queira saber se é bissexto ou não: "))

e()

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto!")
    
else:
    print(f"O ano {ano} não é bissexto!")
    

e()

