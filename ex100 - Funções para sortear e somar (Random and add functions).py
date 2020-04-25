'''
Desafio 100:
Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteio() e somaPar(). A primeria função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores
PARES sorteados pela função anterior.
'''
from random import randint
from time import sleep


def raffle(list):
    print('Raffling five numbers: ',end='')
    sleep(1)
    for i in range(0, 5):
        i = randint(0, 9)
        list.append(i)
        print(f'{i} ',end='')
        sleep(0.5)
    print()


def evensum(list):
    evens = 0
    for val in list:
        if val % 2 == 0:
            evens += val
    print(f'Even number sum from {list} is: {evens}')


number = list()
raffle(number)
sleep(1)
evensum(number)