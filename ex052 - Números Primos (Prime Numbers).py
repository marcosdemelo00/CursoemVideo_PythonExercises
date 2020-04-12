'''
Desafio 052:
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

g = '\033[33m'
r = '\033[31m'
p = '\033[35m'
n = '\033[m'

print('{}|='.format(p)*25+'|{}'.format(n))
print(' '+'\033[7:37m{:^49}\033[m'.format('Prime Number'))
print('{}|='.format(p)*25+'|{}'.format(n))

print('Enter a Integer to know if it is a prime number:')
while True:
    try:
        num = int(input('> ').strip())
        break
    except:
        print('Invalid value.')
        print('Enter a Integer: ',end='')

primetest = int(num ** 0.5)
isprime = True
count = 0
for i in range(2, primetest + 1):
    if num % i == 0:
        isprime = False

if isprime:
    print('The number {} can only be divided by {}1{} or {}itself{}.'.format(num, g, n, g, n))
    print('{}{}{} is a {}PRIME NUMBER{}.'.format(g, num, n, g, n))
else:
    for i in range(1, num + 1):
        if num % i == 0:
            print('{}'.format(g), end=' ')
            count += 1
        else:
            print('{}'.format(r), end=' ')
        print('{}'.format(i), end=' ')

    print('\n{}The number {} was divided {} times.'.format(n, num, count))
    print('{}{}{} is not a {}PRIME NUMBER{}.'.format(r, num, n, r, n))