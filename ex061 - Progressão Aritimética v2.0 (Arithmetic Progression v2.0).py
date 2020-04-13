'''
Desafio 061:
Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os
10 primeiros termos da progressão usando a estrutura while.
'''
from time import sleep

def isfloat(i):
    try:
        i = float(i)
        return True
    except:
        return False


print('+ ' * 17 + '+')
print(' Arithmetic Progression Calculator ')
print('+ ' * 17 + '+')


while True:
    print('Enter the fist value:')
    v = input('> ').strip()
    if isfloat(v) and float(v) > 0:
        v = float(v)
        break
    else:
        print('Invalid Value!\n')
        continue
while True:
    print('Enter the difference:')
    d = input('> ').strip()
    if isfloat(d):
        d = float(d)
        break
    else:
        print('Invalid Value!\n')
        continue

c = 0
sum = 0
while c < 10:
    sum += (v + (d * c))
    print('{:.1f}'.format(v + (d * c)), end='')
    sleep(0.3)
    print(' → ' if c < 9 else '', end='')
    c += 1

print('\nThe sum of that AP is: {}.'.format(sum))
