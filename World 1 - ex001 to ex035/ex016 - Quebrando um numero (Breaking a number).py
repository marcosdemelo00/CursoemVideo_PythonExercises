'''
Desafio 016:
Crie um programa que leia um número Real qualquer pelo teclado e mostre
na tela a sua porção inteira.

Ex.: Digite um número: 6.127
O número 6.127 tem a parte inteira 6
'''


f1 = float(input('Digite um número real: '))
print('O numero digitado foi {} e tem a parte inteira {}'.format(f1, int(f1)))

#ou

from math import trunc
num = f1
print('O número é {} e sua porção inteira é {}'.format(num, trunc(num)))