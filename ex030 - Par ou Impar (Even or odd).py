'''
Desafio 030:
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
'''
from time import sleep

num = input('Enter an integer or you could suffer a misterious accident...\n> ').strip()
joke = 0
while True:
    joke += 1
    if num.isdigit():
        if int(num) % 2 != 0:
            print('WAIT!!!')
            sleep(2)
            print('\nYou are like that ones how likes an ODD number right? Leave Now!')
        else:
            print('Give me a sec...')
            sleep(2)
            print('\nPick your EVEN number and get out!')
        break
    elif joke == 1:
        print('Do you think I have time to loose?')
        num = input('Enter the integer that I asked:\n> ').strip()
    else:
        num = input('Ok, fine... Please The Integer NOW!!\n> ')

