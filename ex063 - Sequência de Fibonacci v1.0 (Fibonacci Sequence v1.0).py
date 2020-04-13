'''
Desafio 063:
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os
n primeiros elementos de uma Sequencia de Fibonacci.

Ex:
0 > 1 > 1 > 2 > 3 > 5 > 8
'''

print('\033[35m' + '#' * 22 + '\033[m')
print('\033[33m  Fibonacci Sequence  \033[m')
print('\033[35m' + '#' * 22 + '\033[m')

while True:
    term = input('How many terms do you want to show? > ').strip()
    try:
        term = int(term)
        if term > 0:
            break
        else:
            print(1/0)
    except:
        print('Invalid value! Please inform a positive integer.\n')

t1 = 0
t2 = 1
t3 = t1 + t2
print('')
if term == t1:
    print('0')
if term == t2:
    print ('0 ⇾ 1')
if term > 2:
    print('0 ⇾ 1', end='')
    for i in range(2, term):
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print(' ⇾ {}'.format(t3), end='')

print('\n\033[35m' + '~' * 22 + '\033[m\n')
