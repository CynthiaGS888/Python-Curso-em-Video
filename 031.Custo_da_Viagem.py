#031.Custo_da_Viagem

import colorama
colorama.init(autoreset=True)

print("="*50)
viagem = float(input("Coloque a distância da viagem em quilômetros: "))
print("="*50)

print(f"\033[34mA viagem será de {viagem}Km.")
if viagem <= 200:
        custo = viagem * 0.5 
        
        print(f"\033[34mA viagem custará \033[31mR${custo:.2f}\033[34m.")

else:
    custo = viagem * 0.45
    
    print(f"\033[34mA viagem custará\033[31m R${custo:.2f}\033[34m.")



print("="*50)