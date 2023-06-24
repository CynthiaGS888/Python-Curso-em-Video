#078.Maior_e_menor_valores_na_lista

num = []

for quant in range(1,6):
    num.append(int(input(f"Digite o {quant}° valor: ")))
    
print(f"Os números digitados foram: {num}")

print(f"O maior número foi {max(num)} na(s) posição(s):  ", end="")
for i, v in enumerate(num):
    if v == max(num):
        print(f"{i} ", end="")
        
print(f"\nO menor número foi {min(num)} na(s) posição(s): ", end="")
for i, v in enumerate(num):
    if v == min(num):
        print(f"{i} ", end="")