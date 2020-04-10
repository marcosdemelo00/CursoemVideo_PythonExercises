'''
Desafio 045:
Crie um programa que faça o computador jogar Jokenpô com você:
'''
from emoji import emojize
from random import choice
from time import sleep

rock = emojize(':fist:', use_aliases=True)
paper = emojize(':hand:', use_aliases=True)
scissors = emojize(':v:', use_aliases=True)

print('\033[1:32mROCK \033[1:30mPAPEL \033[1:37mSCISSORS')
print('\033[1:31m  GAAAAAAAAME!!!\033[m')

while True:
    name = input('Enter your name: ').strip()
    nameok = input('Are you {}? [yes/no]'.format(name)).strip().lower()
    if nameok in ('yes', 'y', ''):
        break

print('\nIt\'s simple, just choose between: \nROCK [R], \nPAPER [P] or \nSCISSORS [S]')
print('and see if you won to me!\n')

print('Now enter: ROCK [R], PAPER [P] or SCISSORS [S]')
yourpoints = 0
pcpoints = 0
round = 0
exit = False
while not exit:
    you = input('Your choice: ').strip().lower()
    pc = choice([rock, paper, scissors])
    if you in ['rock', 'paper', 'scissors', 'r', 'p', 's']:
        if you == 'rock' or you == 'r':
            emo = rock
        elif you == 'paper' or you == 'p':
            emo = paper
        else:
            emo = scissors
    else:
        print('Invalid option.')
        print('Enter: ROCK [R], PAPER [P] or SCISSORS [S]')
        continue

    print('\033[1:31mJO')
    sleep(0.6)
    print('\033[1:32mKEN')
    sleep(0.6)
    print('\033[1:35mPO!!!\033[m')
    sleep(0.3)

    if emo == pc:
        print('{} {} x {} Computer'.format(name, emo, pc))
        print('\033[33mDraw Game\033[m')
    elif emo == rock and pc == paper:
        print('{} {} x {} Computer'.format(name, emo, pc))
        print('\033[31mYou lose!\033[m')
        pcpoints += 1
    elif emo == rock and pc == scissors:
        print('{} {} x {} Computer'.format(name, emo, pc))
        print('\033[34mYou won!\033[m')
        yourpoints += 1
    elif emo == paper and pc == scissors:
        print('{} {} x {} Computer'.format(name, emo, pc))
        print('\033[31mYou lose!\033[m')
        pcpoints += 1
    elif emo == paper and pc == rock:
        print('{} {} x {} Computer'.format(name, emo, pc))
        print('\033[34mYou won!\033[m')
        yourpoints += 1
    elif emo == scissors and pc == rock:
        print('{} {} x {} Computer'.format(name, emo, pc))
        print('\033[31mYou lose!\033[m')
        pcpoints += 1
    elif emo == scissors and pc == paper:
        print('{} {} x {} Computer'.format(name, emo, pc))
        print('\033[34mYou won\033[m!')
        yourpoints += 1

    round += 1
    while True:
        again = input('Do you want to try again? [yes/no]').strip().lower()
        if again == 'yes' or again == 'y' or again == '':
            break
        elif again == 'no' or again == 'n':
            exit = True
            break
        else:
            print('Invalid option.')


if yourpoints > pcpoints:
    print('\nCongratulations {}. \033[34mYou WON!\033[m\n '
          '{} Rounds: You {} x {} Computer'.format(name, round, yourpoints, pcpoints))
elif yourpoints == pcpoints:
    print('\nIt\'s OK {}. \033[33mYou TIED!\033[m\n '
          '{} Rounds: You {} x {} Computer'.format(name, round, yourpoints, pcpoints))
else:
    print('\nI\'m sorry {}. \033[31mYou LOSE\033[m!\n '
          '{} Rounds: You {} x {} Computer'.format(name, round, yourpoints, pcpoints))