'''
Desafio 099:
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep


def line():
    print('-' * 40)


def bigger(* num):
    big = count = 0
    print(f'From the numbers: ',end='')
    for n in num:
        sleep(0.25)
        print(f'{n} ', end='')
        count += 1
        if n > big:
            big = n
    print('\n'f'There are {count} values.''\n'f'The Biggest is {big}.')

line()
bigger(1, 4, 7, 2, 5, 8, 2, 9, 12, 28)
line()
bigger(78, 429, -236, 42)
line()
bigger()
line()
