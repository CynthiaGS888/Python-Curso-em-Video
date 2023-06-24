#036.Impréstimo_bancário

valor = float(input("Qual o valor da casa? "))

salário = float(input("Qual o seu salário? "))

qntanos = float(input("Em quantos anos vai pagar? "))

prestação = valor / (12 * qntanos)


if prestação > salário * 0.30:
    print(f"Para pagar uma casa de R${valor} em {qntanos:.0f} anos, com a prestação de R${prestação:.2f}, você precisaria ganhar mais.\nEmpréstimo negado. ")
    
else:
    print(f"A prestação será de R${prestação:.2f}")
    print("Parabéns! Seu empréstimo foi aprovado!")