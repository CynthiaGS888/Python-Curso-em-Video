#060.Cálculo_de_fatorial

num = int(input("Coloque um número para ver seu fatorial: "))

calc = 1

for c in range(1, num+1):
    calc *= c
    
print(f"O fatorial de {num} é: {calc}.")

#--------------------------------------------------------------

quant = 1
calc2 = 1

while quant != num + 1:
    calc2 *= quant
    quant +=1
    
print(calc2)

#--------------------------------------------------------------
print("="*30)
c = num
f = 1
print(f"Calculando {num}! =", end=" ")
while c > 0:
    print(f"{c}", end=" ")
    print("x" if c > 1 else "=", end=" " )
    f *= c
    c -= 1
print(f"{f}")
    