'''
Desafio 058:
Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre
0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
'''
from time import sleep
from random import randint

comp = 0
rounds = 0
num = ''

print('\033[1:7:32m*\033[m' * 37)
print('            GUESSING GAME')
print('\033[1:7:33m*\033[m' * 37)
sleep(1)
print('\nHello my dear friend!')
sleep(0.5)
print('This is the Guessing Game!')
sleep(0.5)
print('It\'s simple, I think in one number from 0 to 10,')
sleep(0.5)
print('and you try to guess what number it is!\n')
start = input('Are you ready? [Yes/No] > ').strip().lower()

if start not in ('yes', 'y', ''):
    print('Come on... Let\'s play...')
    start = input('Shall we start now? [Yes/No] > ').strip().lower()

exit = False
if start in ('yes', 'y', ''):
    print('\nLet\'s GOOOOO!')
    sleep(1)
    while not exit:
        print('I\'m thinking in a number... What is it?')
        comp = randint(0,11)
        while True:
            rounds += 1

            while True:
                num = input('Try [0 to 10] > ').strip()
                sleep(0.5)
                if num.isdigit() and int(num) <= 10:
                    num = int(num)
                    break
                else:
                    print('Bzzzzzzzzzz')
                    sleep(1.5)
                    print('I\'m really thinking in a number from 0 to 10...')
                    continue

            if num > comp:
                print('Wah', end=', ')
                sleep(0.3)
                print('wah', end=', ')
                sleep(0.3)
                print('Wahhhhhhh...')
                sleep(0.6)
                if rounds == 1:
                    print('Wrong! Try a smaller number:')
                else:
                    print('Wrong again! Try a smaller number:')
                continue
            elif num < comp:
                print('Wah', end=', ')
                sleep(0.3)
                print('wah', end=', ')
                sleep(0.3)
                print('Wahhhhhhh...')
                sleep(0.6)
                if rounds == 1:
                    print('Wrong!, Try a bigger number:')
                else:
                    print('Wrong again! Try a bigger number:')
            else:
                print('Tah', end=', ')
                sleep(0.5)
                print('tah', end=', ')
                sleep(0.2)
                print('Dahhhhhhh!!!')
                sleep(1)
                print('\nCongratulations! You got it!')
                if rounds <= 3:
                    print('In just {} rounds!'.format(rounds))
                elif rounds <= 6:
                    print('In {} rounds.'.format(rounds))
                else:
                    print('But... that was {} rounds...'.format(rounds))
                break
        sleep(0.5)
        again = input('\nDo you want to play again? [Yes/No]: ').strip().lower()
        print('')
        if again in ('yes', 'y', ''):
            continue
        else:
            exit = True

    print('That was nice to play with you!\nLet\'s play more another time!')
else:
    print('')
    for i in range(0, 5):
        print('.', end='')
        sleep(0.5)
    print('.')
    sleep(1)
    print('Ok then... We can play another time.')

