#044.Gerenciador_de_pagamentos

def e():
    print("-"*43)

print(f"{' Bem vindes ':=^43}")
print("============== Loja do Tadeu ==============")

preço = float(input("Coloque o preço das compras! R$"))
e()
print('''Coloque a forma de pagamento:
(1) À vista em dinhero / cheque
(2) À vista no cartão
(3) Em 2x no cartão
(4) Em 3x ou mais no cartão''')

pag = int(input("Qual sua opção? "))
e()

if pag == 1:
    preço = preço - (preço * 0.10)
    print(f"Com essa opção, você ganhou 10% de desconto, totalizando R${preço:.2f}!")
    e()

elif pag == 2:
    preço = preço - (preço * 0.05)
    print(f"Com essa opção, você ganhou 5% de desconto, totalizando {preço:.2f}!")
    e()

elif pag == 3:
    prest = preço / 2
    print(f"Com essa opção, você irá pagar em prestações de R${prest:.2f}, totalizando R${preço:.2f}.")
    
elif pag == 4:
    div = int(input("Em quantas prestações? "))
    totalj = preço + (preço * div * 0.2)
    prestação = totalj / div
    
    print(f"Com essa opção, você irá pagar {div} prestações de R${prestação:.2f}, adicionando o 20% de juros, totalizando R${totalj:.2f}.")

else:
    print("Opção inválida de pagamento, tente novamente.")