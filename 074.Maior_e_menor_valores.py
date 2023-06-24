#074.Maior_e_menor_valores

from random import randint

números =  tuple(randint(0,10) for num in range (5))
    
print(números)

maior = números[0]
menor = números[0]

for num in números[1:]:
    if num > maior:
        maior = num
    
    if num < menor:
       menor = num
        

print(f"O maior número foi {maior}\nO menor número foi {menor}")