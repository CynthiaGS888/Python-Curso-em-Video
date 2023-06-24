#021.Tocando_mp3
import colorama
colorama.init(autoreset=True)
from time import sleep
import winsound

pergunta = str(input("Quer ouvir uma música [S/N]? ")).upper().strip()[0]

if pergunta == "S":
    print("-"*50)
    print("\033[35mCarregando música", end="")
    sleep(1)
    print("\033[35m.",end='')
    sleep(1)
    print("\033[35m.",end='')
    sleep(1)
    print("\033[35m.")
    print("-"*50)
    
    print(f"{' TOCANDO AGORA: ':^50}")
    print(f"{' Never goona give you up ':^50}")
    print("-"*50)
    winsound.PlaySound(r'C:\Users\Cynthia\Python\Refazendo os exercícios!\021.song.wav', winsound.SND_FILENAME)
  
elif pergunta == "N":
    print("Que pena :/")