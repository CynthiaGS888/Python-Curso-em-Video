#083.Validando_expressões_matemáticas

expressão = str(input("Digite uma expressão: "))

pilha = []

for l in expressão:
    if l == "(":
        pilha.append("(")   
        
    elif l == ")":
        if len(pilha) > 0:
            pilha.pop()
            
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("Sua expressão está válida!")

else:
    print("Sua expressão não está válida!")        