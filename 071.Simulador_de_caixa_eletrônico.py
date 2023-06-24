#Simulador_de_caixa_eletrônico

def e():
    print("="*50)

cinquenta = vinte = dez = um = 0

e()
print(f"{'Banco Python':^50}")
e()

valor = int(input("Qual o valor que deseja sacar? R$"))
e()

while valor > 0:
    if valor >= 50:
        cinquenta += 1
        valor -=50
    
    elif valor >= 20:
        vinte += 1
        valor -= 20
    
    elif valor >= 10:
        dez += 1
        valor -= 10
    
    elif valor >= 1:
        um += 1
        valor -= 1

print(f"Total de {cinquenta} notas de R$50")
print(f"Total de {vinte} notas de R$20")
print(f"Total de {dez} notas de R$10")
print(f"Total de {um} notas de R$1")
e()