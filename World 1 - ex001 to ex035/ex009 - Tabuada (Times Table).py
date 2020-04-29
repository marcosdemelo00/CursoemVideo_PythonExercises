'''
Desafio 009:
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua
tabuada.
'''
n = 1
while n == 1:
    try:
        tab = int(input('Insert a integer and get it\'s table: '))
        n += 1
    except:
        print('Enter a valid value.')

print('The table of {} is:'.format(tab))
print('=' * 13)
for v in range(1, 11):
    print(' {} x {:>2} = {}'.format(tab, v, tab * v))
print('=' * 13)
