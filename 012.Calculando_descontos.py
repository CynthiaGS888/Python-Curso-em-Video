#012.Calculando_descontos
import colorama
colorama.init(autoreset=True)

def e():
    print("\033[34m-"*50)
    
e()
print(f"{' Mercadinho do Python ':^50}")
e()

nome = str(input("Coloque o nome do produto: ")).strip().lower()
preço = float(input("Coloque o preço do produto: "))
e()
desconto = preço - (preço * 0.05)
print(f"O produto {nome} com 5% de desconto dá R${desconto:.2f}.")
e()