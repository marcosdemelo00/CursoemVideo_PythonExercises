'''
Desafio 096:
Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''


def area(x, y):
    print(f'A land with width of {x}m and a length of {y}m has an area of {x * y:.1f}m²')


while True:
    try:
        width = float(input('Enter land width: ').strip())
        length = float(input('Enter land length: ').strip())
        break
    except:
        continue
area(width, length)
