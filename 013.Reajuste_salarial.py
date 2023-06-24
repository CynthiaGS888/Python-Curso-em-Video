#013.Reajuste_salarial
import colorama
colorama.init(autoreset=True)

salário = float(input("Coloque o seu salário: "))

aumento = salário + (salário * 0.15)

print(f"\033[33mParabéns! Você ganhou um aumento!\033[m\nSeu salário foi de R${salário} para \033[32mR${aumento}.")
