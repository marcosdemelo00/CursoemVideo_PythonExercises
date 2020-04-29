'''
Desafio 067:
Faça um programa que mestre a tabuada de vários números, um de cada vez,
para cada malor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.
'''

print('_-' * 17)
print('  Multiplication Table Generator  ')
print('-_' * 17)
while True:
    while True:
        try:
            n = int(input('What number do you want to see the table? [ <= 0 to leave]\n Table of: ').strip())
            break
        except ValueError:
            print('Invalid value. Enter a Integer.')

    if n <= 0:
        break

    print('*' * 24)
    count = 0
    for n in range(1, 11):
        print(f'{n} x {count:>2} = {n * count}')
        count += 1
    print('*' * 24)

print('\n' + '_' * 42)
print(' Multiplication Table Generator Finished!')
print('_' * 42)
