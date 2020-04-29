'''
Desafio 049:
Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço For.
'''
from time import sleep


print('\033[7:34m MULTIPLICATION TABLE \033[m')
while True:
    n = input('\nEnter a number to see his multiplication table:\n> ').strip()
    if n.isdigit():
        n = int(n)
        break
    else:
        print('Invalid value!\n')
        sleep(1)
        continue

for t in range(1, 11):
    print('{} x {:>2} = {}'.format(n, t, t * n))