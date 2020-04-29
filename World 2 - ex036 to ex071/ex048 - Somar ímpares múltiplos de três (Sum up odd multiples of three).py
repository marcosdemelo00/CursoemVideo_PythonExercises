'''
Desafio 048:
Faça um programa que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
from time import sleep

sumc = 0
count = 0
print('''I will show all the \033[3:32modd numbers\033[m
that are multiples of three
in \033[34m1\033[m to \033[34m500\033[m and the \033[3:32msum of them\033[m:\n''')
sleep(1)
for c in range(3, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        sleep(0.1)
        sumc += c
        count += 1

print('\n\nSoo... There are {} numbers\n'
      'and the sum is {}'.format(count, sumc))
