'''
Desafio 113:
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
possibilidade da digitação de um número do tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''


def readint(msg):
    while True:
        try:
            i = int(input(msg).strip())
        except ValueError:
            print('\033[31mERROR: Invalid value!\033[m')
        except KeyboardInterrupt:
            print('\033[33mProgram interrupted by user.')
            return ''
        else:
            return i


def readfloat(msg):
    while True:
        try:
            f = float(input(msg).strip())
        except ValueError:
            print('\033[32mERROR: Invalid value!\033[m')
        except KeyboardInterrupt:
            print('\033[33mProgram interrupted by user.')
            return ''
        else:
            return f


i = readint('Enter a Integer: ')
f = readfloat('Enter a Float: ')
if i != '' and f != '':
    print(('-' * 40) + f'\nInteger value is {i}, float value is {f:.1f}.\n' + ('-' * 40))
