'''
Desafio 074:
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
'''
from random import randint

input('Press Enter to generate 5 random numbers...')
tup = ()
for n in '12345':
    r = randint(1, 100)
    tup += (r,)

low = hi = 0
for n in tup:
    if n > hi:
        hi = n
    if n < low or low == 0:
        low = n

print(f'The number generated are {tup}')
print(f'The highest number is {hi}')
print(f'The lowest number is {low}')
print(f'min {min(tup)}; max {max(tup)}')