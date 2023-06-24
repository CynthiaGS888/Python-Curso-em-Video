import colorama
colorama.init(autoreset=True)

print("\033[36m=" * 60)
num = float(input("Escolha um número para ver seu antecessor e sucessor: "))
print("\033[36m=" * 60)
print(f"O número escolhido foi: \033[35m{num}\033[m\nSeu antecessor é: \033[35m{num-1}\033[m\nSeu sucessor é: \033[35m{num+1}\033[m")
print("\033[36m=" * 60)