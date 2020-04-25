'''
Desafio 106:
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai
digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
'FIM', o programa encerrará.

Obs: Use cores.
'''
from time import sleep


def helper(command):
    print('\033[1:7:33m' + '~' * (29 + len(command)))
    print(f'\033[40m  Accessing command {command} manual  \033[43m')
    print('\033[48m' + '~' * (29 + len(command)))
    print('\033[m')
    sleep(1)
    print('\033[1:7m')
    help(command)
    print('\033[m')


while True:
    print('\033[1:7:34m' + '-' * 22)
    print('  HELP SYSTEM PyHELP  ')
    print('-' * 22)
    h = input('\033[:34mCommand or library: [END to finish]\n >>>  ').strip().lower()
    if h == 'end':
        break
    else:
        helper(h)
print('Finishing.', end='')
for i in range(0, 5):
    sleep(0.3)
    print('.', end='')
