#096.Função_que_calcula_área
def area(a, b):
    Area = a * b
    print(f'A área de {a}m por {b}m é {Area}m²')


print('='*50)
print(f'{"CALCULADORA DE ÁREA":^50}')
print('='*50)

largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))



area(largura, comprimento)