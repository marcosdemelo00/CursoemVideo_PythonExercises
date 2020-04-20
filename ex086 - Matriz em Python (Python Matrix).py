'''
Desafio 086:
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela com a formatação correta.
'''
def num(x, y):
    while True:
        try:
            n = float(input(f'Enter value ({x}, {y}): ').strip())
            return n
        except:
            continue


print('\n| My first Matrix |')

matrix = [[],[],[]]
for x in range(0,3):
    for y in range(0,3):
        matrix[x].append(num(x, y))
print()

for x in range(0, 3):
    for y in range(0, 3):
        if y == 2:
            print(f'[{matrix[x][y]:^5}]', end='\n')
        else:
            print(f'[{matrix[x][y]:^5}]|', end='')