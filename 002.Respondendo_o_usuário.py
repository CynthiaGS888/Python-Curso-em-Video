#002.Respondendo_o_usuário
import colorama
colorama.init(autoreset=True)


print("="*30)
genero = input("Com qual gênero se identifica [M/F/N]? ").upper().strip()[0]
nome = str(input("Digite seu nome: "))

print("="*30)
if genero == "M":
    print(f"\033[31mSeja bem vindo {nome}!")
    print("="*30)
elif genero == "F":
    print(f"\033[31mSeja vem vinda {nome}!")
    print("="*30)
else:
    print(f"\033[31mSeja bem vinde {nome}!")
    print("="*30)