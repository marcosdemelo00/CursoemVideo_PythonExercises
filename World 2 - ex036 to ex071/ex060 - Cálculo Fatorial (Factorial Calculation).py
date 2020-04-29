'''
Desafio 060:
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120
'''

while True:
    print('Enter a Integer to know it\'s fatorial:')
    num = input('> ').strip()
    if num.isdigit() and int(num) >= 0:
        num = int(num)
        numw = num
        countw = num
        break
    else:
        print('Invalid Value!\n')

# WHILE
print('{}! = '.format(numw), end='')
while countw > 1:
    print('{} x '.format(countw), end='')
    countw -= 1
    numw *= countw
print('1 = {}'.format(numw))

#FOR
numf = 1
print('{}! = '.format(num), end='')
for i in range(num, 0, -1):
    numf *= i
    print(i, end='')
    print(' x ' if i > 1 else ' = ', end='')
print(numf)
