#076.Lista_de_preço_tupla

lista = ("maçã", 5.00), ("lápis", 1.00), ("Caderno", 20.00)

print("="*30)
print(f"{' Lojinha Python ':^30}")
print("="*30)

for item, preço in (lista):
    print(f"{item:.<20} R$ {preço:>5.2f}") 
    
print("="*30)
