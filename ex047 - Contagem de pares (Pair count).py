'''
Desafio 047:
Crie um programa que mostre na tela todos os números pares que estão no intervalo
entre 1 a 50.
'''
from time import sleep

print('I will just show you all pair numbers from 1 to 50')
sleep(2)
for c in range(2, 51, 2):
    print(c, end=' ')
    sleep(0.25)
print('\nAnd that is it...')