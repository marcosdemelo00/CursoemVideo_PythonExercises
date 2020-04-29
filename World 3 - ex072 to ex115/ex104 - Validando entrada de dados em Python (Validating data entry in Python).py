'''
Desafio 104:
Crie um programa que tenh aa função leiaint(), que vai funcionar de formar
semelhante à função input() do Python, só que fazendo a validação para aceitar
apenas um valor numérico.

Ex:
n = leiaInt('Digite um n')
'''


def enterInt(t):
    while True:
        integ = input(f'{t}')
        if integ.isnumeric():
            return int(integ)
        else:
            print('\033[31mERROR! Enter a valid integer.\033[m')


num = enterInt('Enter a number: ')
print(f'You entered number {num}.')