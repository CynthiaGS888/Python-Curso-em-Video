print("="*50)

num = (int(input("Digite o primeiro número: ")),
       int(input("Digite o segundo número: ")),
       int(input("Digite o terceiro número: ")),
       int(input("Digite o quarto número: ")))

print("="*50)

print(f"Você digitou os valores: {num}")
print(f"Apareceram {num.count(9)} vezes o número nove.")
if 3 in num:
    print(f"O número três apareceu na {num.index(3)+1}ª posição.")
else:
    print("Não há 3.")
print("Os números pares são: ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end=" ") 

print("\nAcabou!")     
print("="*50)