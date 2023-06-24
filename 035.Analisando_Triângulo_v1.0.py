#035.Analisando_Triângulo_v1.0

import colorama
colorama.init(autoreset=True)

def e():
    print("\033[35m="*70)
    
e()
print(f"{' FORMA UM TRIÂNGULO? ':~^70}")
e()

print(f"{'Me dê três segmentos de reta e eu digo se forma um triângulo!':^70}")

print(" ")

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

e()

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: 
    print(f"Os segmentos {r1}, {r2} e {r3}\033[32m podem sim\033[m formar um triângulo!")

else: 
    print(f"Os segmentos {r1}, {r2} e {r3}\033[31m não pode \033[m formar um triângulo :/")
    

e()