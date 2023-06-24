#094.Unindo_dicionários_e_listas
grupo = list()
pessoa = dict()

soma = 0


while True:
    print('='*50)
    
    pessoa.clear()
    
    pessoa['Nome'] = str(input('Digite o nome: '))
    
    while True:
        pessoa['Sexo'] = str(input('Digite o sexo: ')).upper()[0]
        if pessoa['Sexo'] not in 'FM':
            print("A resposta pode ser apenas F ou M.")
        else:
            break
        
    pessoa['Idade'] = int(input('Digite a idade: '))
    
    grupo.append(pessoa.copy())
    
    while True:
        pergunta = str(input('Deseja continuar [S/N]? ')).upper()[0]
        if pergunta not in 'SN':
            print("A reposta pode ser apenas S ou N.")
        else:
            break

    if pergunta == "N":
        break   
     
print('='*50)
print(grupo)
print('='*50)

print(f'Foram cadastradas {len(grupo)} pessoas. Dessas {len(grupo)} pessoas:')

for pessoa in grupo:
    soma += pessoa['Idade']

media = soma / len(grupo)

print(f'  ---> A média de idade é {media:.2f} anos.')

print(f'  ---> As mulheres cadastradas são:', end=' ')
for pessoa in grupo:
    if pessoa['Sexo'] == "F":
        print(f'{pessoa["Nome"]}', end=' ')

print(" ")

print(f'  ---> As pessoas com idade acima da média são:', end=' ')
for pessoa in grupo:
    if pessoa['Idade'] > media:
        print(f"{pessoa['Nome']}", end=' ')
        
print(" ")
print("="*50)