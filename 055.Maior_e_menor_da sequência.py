#055.Maior_e_menor_da sequência
def e():
    print("="*30)


pesos = []


e()
for pess in range(1,6):
    peso = float(input(f"Coloque o peso da {pess}° pessoa: "))
    pesos.append(peso)
e()

print(f"O menor peso é: {min(pesos)}Kg\nO maior peso é: {max(pesos)}Kg")
e()