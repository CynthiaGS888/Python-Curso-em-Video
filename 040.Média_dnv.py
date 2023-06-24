#040.Média_dnv
import colorama
colorama.init(autoreset=True)

def e():
    print("==" * 30)

e()
print("\033[35mColoque suas notas para calcular sua média!")

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
e()

média = (n1 + n2) / 2

print(f"Sua média é: {média:.1f}.")

if média < 5:
    print("\033[31mVocê foi infelizmente reprovado.")
    e()
    
elif média >= 5 and média < 6.9:
    print("\033[33mVocê está em recuperação.")
    e()

elif média >= 7:
    print("\033[32mVocê foi aprovado!")
    e()