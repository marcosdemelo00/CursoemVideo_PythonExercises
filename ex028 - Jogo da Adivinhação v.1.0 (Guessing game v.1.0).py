'''
Desafio 028:
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint


def notjokes(t):                    # To avoid invalid values
    while True:
        v = input('{}>>>'.format(' ' * 8)).strip()
        t += 1
        if v.isdigit() and int(v) >= 0 and int(v) <= 5:
            break
        elif t == 1:
            print(f'{"That is not an integer from 0 to 5, try again:":^60}')
        elif t == 2:
            print(f'{"Pay attention, I am thinking in an integer from 0 to 5:":^60}')
        elif t == 3:
            print(f'{"We are not going to anywhere":^60}')
            print(f'{"if you continue breaking the rules...":^60}')
        elif t == 4:
            print(f'{"Come on... I will be waiting for an integer from 0 to 5...":^60}')
    return v

print('-=-' * 20)                   # Game title
title = '      Guessing Game     '
rtitle = ('{:>>{l}}'.format(title, l = 30 + (int(len(title)/2))))
print('{:<<60}'.format(rtitle))
print('-=-' * 20)
print(f'{"Hello, Wellcome to the Guessing Game".center(60)}')
print(f'{"The Rules are simple:":^60}')
print('\n{}1. I wil think in an integer from 0 to 5\n'
      '{}2. You try to guess what number I\'m thinking'.format(' '*8,' '*8),end='\n')
print('\n{:^60}\n{:^60}'.format('Let\'s start!!', 'Soo... Try to guess what number I\'m thinking.'))


mynum = randint(0, 5)               # Computer's Number
guess = notjokes(0)                 # User's Number

while True:                         # Comparing the values
    if int(guess) == mynum:
        print('{:^60}'.format('Congratulations! It\'s ' + guess + '!'))
        print(f'{"You Guessed my number.":^60}')
        break
    else:
        print(f'{"You wrong! try again:":^60}')
        guess = notjokes(5)
