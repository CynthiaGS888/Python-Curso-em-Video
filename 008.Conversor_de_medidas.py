#008.Conversor_de_medidas
import colorama
colorama.init(autoreset=True)

def e():
    print("\033[31m="*50)
    


print(f"\033[31m{' CONVERSOR DE MEDIDAS ':=^50}")

metros = int(input("Quantos metros quer converter? "))
e()

print(f"\033[33mEm quilômetro: {metros/1000}km")
print(f"\033[33mEm hectômetro: {metros/100}hm")
print(f"\033[33mEm decâmetro: {metros/10}dam")
print(f"\033[32mEm metros: {metros}m")
print(f"\033[36mEm decímetro: {metros*10}dm")
print(f"\033[36mEm centímetro: {metros*100}cm")
print(f"\033[36mEm milímetro: {metros*1000}mm")

e()