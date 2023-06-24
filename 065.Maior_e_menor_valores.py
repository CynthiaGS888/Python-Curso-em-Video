#065.Maior_e_menor_valores
contador = 0
soma = 0
numbers = []


while contador < 10:
    num = int(input("Coloque um número inteiro: "))
    numbers.append(num)
    contador += 1
    soma += num
    continuar = input("Deseja continuar [S/N]?" ).lower()
    
    if continuar == "s":
        continue
    else: 
        break

média = soma / contador

print(f"Foram pedidos {contador} números.")
print(f"A média de todos os números somados foi de {média}")
print(f"O maior número é: {max(numbers)}\nO menor número é: {min(numbers)}")

