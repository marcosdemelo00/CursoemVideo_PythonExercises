'''
Desafio 115:
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome
e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: acadastrar uma nova pessoa e listar todas as
pessoas cadastradas.
'''

from time import sleep
from ex115.menu import *
from ex115.txt import *

file = 'ex115register.txt'
size = 40
while True:
    option = menu(['Register new person',
                   'List Registered persons',
                   'Exit program'], size)

    if option == 1:
        while True:
            name = input('Full name: ').strip()
            age = readint('Age: ')
            valid = areyousure(name, age, size)
            if valid:
                break
        register(file, name, age, size)
        sleep(1)
    elif option == 2:
        sleep(0.3)
        readfile(file, size)
    elif option == 3:
        sleep(0.5)
        print('\n\033[34mFinishing program', end='')
        for i in range(0, 3):
            print('.', end='')
            sleep(0.5)
        print('\033[m')
        break


sleep(1)
print('\n\033[1:7:34m' + 'See you later!'.center(size) + '\033[m')