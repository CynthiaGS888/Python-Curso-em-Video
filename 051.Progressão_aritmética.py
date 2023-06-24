#051.Progressão_aritmética

n = int(input("Coloque o primeiro número, para ver sua progressão aritmética: "))
r = int(input("Coloque a razão: "))
décimo = n + (10 - 1) * r


for c in range(n, décimo + r, r):
    print(c, end=" \032 ")
    
print("ACABOU")