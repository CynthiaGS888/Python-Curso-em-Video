#062.Sequência_de_fibonacci

'''num = int(input("Coloque o primeiro termo, para ver sua sequência de fibonacci: "))
termos = int(input("Quantos termos quer na sequência: "))

f = 0
seq = 0


while seq < termos:
    num2 = num + f
    prevnum = num
    num = f
    f = prevnum + f
    seq += 1
    print(num2, end=" \032 ")

print("Fim.")
    '''

n = int(input("Quantos termos quer mostrar? "))

cont = 3
t1 = 0
t2 = 1

print(f"{t1} \032 {t2}", end=" ")

while cont != n + 1:
    t3 = t1 + t2
    cont += 1 
    print(f"\032 {t3}", end=" ")
    t1 = t2
    t2 = t3
    
print("\032 Fim.")