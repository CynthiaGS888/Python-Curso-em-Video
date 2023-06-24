#090.Dicionário_em_Python
print('~'*50)
print(f"{'Calculo de média':^50}")
print('~'*50)

nome = str(input('Digite o nome do aluno: '))
media = float(input('Digite sua média: '))

print('~'*50)

boletim = {'Nome':nome, 'Média':media}

if media >= 6:
    boletim['Resultado'] = 'Aprovado'
    
else:
    boletim['Resultado'] = 'Reprovado'
    

for k, v in boletim.items():
    print(f'{k} = {v}')
    
print('~'*50)