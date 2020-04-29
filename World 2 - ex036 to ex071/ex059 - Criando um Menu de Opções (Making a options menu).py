'''
Desafio 059:
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair
Seu programa deverá realizar a operação solicitada em cada caso.
'''

def isfloat(f):
    try:
        f = float(f)
        return True
    except:
        return False


exit = False
while not exit:
    print('Enter two values:')
    while True:
        v1 = input('\033[33m1st\033[m value: ').strip()
        v2 = input('\033[34m2nd\033[m value: ').strip()
        if isfloat(v1) and isfloat(v2):
            v1 = float(v1)
            v2 = float(v2)
            break
        else:
            print('Invalid Values!\n')

    while True:
        i = '\033[7m'
        n = '\033[m'
        print(i + ' ' + '=' * 16 + ' ' + n)
        print('{}{:^18}{}'.format(i, '|Menu|', n))
        print(i + ' ' + '-' * 16 + ' ' + n)
        print('{}{:<18}{}\n{}{:<18}{}\n{}{:<18}{}\n{}{:<18}{}\n{}{:<18}{}'
              .format(i, '  [1] Add', n, i, '  [2] Multiply', n, i,
                      '  [3] Bigger', n, i, '  [4] New values',n, i, '  [5] Exit', n))
        print(i + ' ' + '-' * 16 + ' ' + n, end='\n')
        opt = input('What is your choice: ').strip().lower()

        if opt in ('5', 'e', 'exit'):
            exit = True
            break
        elif opt in ('4', 'n', 'new values'):
            break
        elif opt in ('3', 'b', 'bigger'):
            if v1 == v2:
                print('1st value: \033[33m{}\033[m and '
                      '2nd value: \033[34m{}\033[m are equal.'.format(v1, v2))
            elif v1 > v2:
                print('1st Value: \033[33m{}\033[m is bigger than '
                      '2nd value: \033[34m{}\033[m.'.format(v1, v2))
            else:
                print('2nd value: \033[34m{}\033[m is bigger than '
                      '1st value: \033[33m{}\033[m.'.format(v2, v1))
        elif opt in ('2', 'm', 'multiply'):
            print('1st value: \033[33m{}\033[m multiplied by the '
                  '2nd values: \033[34m{}\033[m is equal to: '
                  '\033[1:37m{}\033[m'.format(v1, v2, v1 * v2))
        elif opt in ('1', 'a', 'add'):
            print('1st value: \033[33m{}\033[m plus '
                  '2nd value: \033[34m{}\033[m is equal to: '
                  '\033[1:37m{}\033[m'.format(v1, v2, v1 + v2))
        else:
            print('Invalid Option.')

print('Exiting...')