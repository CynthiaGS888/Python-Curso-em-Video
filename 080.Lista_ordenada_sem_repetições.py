#080.Lista_ordenada_sem_repetições
numeros = []

for c in range (1,6):
    n = int(input("Digite um número: "))
    if c == 1:
        numeros.append(n)
    else:
        if n > max(numeros):
            numeros.append(n)
            print("Adicionado no final da lista..")

        elif n < min(numeros):
            numeros.insert(0, n)
            print("Adicionado no início da lista..")
            
        else:
           pos = 0
           while pos < len(numeros):
               if n <= numeros[pos]:
                   numeros.insert(pos, n)
                   print(f"Adicionado na posição {pos+1} da lista")
                   break
               
               pos += 1
               
               
print(f"Os valores digitados foram: {numeros}")
        