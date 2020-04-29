'''
Desafio 062:
Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns
termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''
from time import sleep
def rnum(f, t):
    rf = input('{}'.format(f)).strip()
    try:
        if t == 'f':
            rf = float(rf)
        elif t == 'i':
            rf = int(rf)
        return rf
    except:
        print('Invalid value')
        sleep(0.3)
        rnum(f, t)


def ap():
    for c in range(counti, countf):
        print('\033[32m{}\033[m'.format(first + (diff * c)), end='')
        print(' > ' if c < (countf - 1) else '', end='')
        sleep(0.3)


print('\033[33m' + ' +' * 22 + ' \033[m')
print(' Arithmetic Progression Calculator Extended ')
print('\033[33m' + ' +' * 22 + ' \033[m\n')

counti = 0
countf = 10
first = rnum('Enter the first term: ', 'f')
diff = rnum('Enter the difference: ', 'f')
ap()

while True:
    print('')
    term = rnum('How many terms do you want to show more?\n > ', 'i')
    counti = countf
    countf += term
    if term != 0:
        ap()
    else:
        break

print('Arithmetic Progression Calculator Extended finished.')
print('\033[33m{}\033[m terms were shown.'.format(countf))
