#001.Olá_Mundo

import colorama
import winsound

colorama.init(autoreset=True)



print("\033[34m="*50)
print(f"\033[31m{' Olá mundo! ':=^50}")
print("\033[34m="*50)

winsound.PlaySound(r'C:\Users\Cynthia\Python\Refazendo os exercícios!\musica.wav', winsound.SND_FILENAME)