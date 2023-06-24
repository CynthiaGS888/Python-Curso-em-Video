#029.Radar_eletrônico

import colorama
colorama.init(autoreset=True)

velocidade = float(input("Digite a velocidade do carro em quilômetros: "))

print(f"\033[33mSua velocidade atual é de {velocidade}Km/h, o máximo permitido é 80km/h.",end=" ")

if velocidade > 80:
    velocidade = (velocidade - 80) * 7
    
    print(f"\033[31mVocê ultrapassou o limite! \n\033[31mSua multa será de R${velocidade:.2f}! ")

else:
    print("\033[32mEstá dirigindo dentro do limite.\nTenha um bom dia :D")