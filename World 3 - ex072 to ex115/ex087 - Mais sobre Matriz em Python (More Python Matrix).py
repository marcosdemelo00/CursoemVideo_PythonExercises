'''
Desafio 087:
Aprimore o desafio anterior, Desafio 086, mostrando no final:
a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.
'''

def num(x, y):
    while True:
        try:
            n = float(input(f'Enter a value ({x}, {y}): ').strip())
            return n
        except:
            continue
print('=)(=' * 8)
print('\n|| My second Matrix ||')
print('(==)' * 8)

m = [[], [], []]
for x in range(0, 3):
    for y in range(0, 3):
        m[x].append(num(x, y))

print('=)(=' * 8)

even = trdcol = seclbig = 0
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{m[x][y]:^5}]', end='')
        if m[x][y] % 2 == 0:
            even += m[x][y]
        if y == 2:
            trdcol += m[x][y]
        if x == 1 and m[x][y] > seclbig:
            seclbig = m[x][y]
    print()

print('(==)' * 8)
print(f'The sum of even values is: {even}')
print(f'The third column sum value is: {trdcol}')
print(f'The second line bigger value is: {seclbig}')