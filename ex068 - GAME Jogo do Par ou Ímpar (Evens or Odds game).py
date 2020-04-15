'''
Desafio 068:
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo.
'''
from random import randint

print('Let\' play EVEN or ODD.')
woncount = 0
while True:
    while True:
        choice = input('Do you want EVEN or ODD? (E/O) _').strip().lower()
        if choice in ('even', 'odd', 'e', 'o'):
            break

    while True:
        num = input('Chose your number: [0 to 10] _').strip()
        if int(num) in range(0, 11):
            num = int(num)
            break

    comp = randint(0, 10)
    if num + comp == 0:
        print(f'You 0 + 0 Computer')
        print(f'Oh... Draw round')
    elif ((num + comp) % 2) == 0:
        if choice in ('even', 'e'):
            print(f'You {num} + {comp} Computer')
            print(f'{num + comp} is Even! You Won!')
            woncount += 1
        else:
            print(f'You {num} + {comp} Computer')
            print(f'{num + comp} is Even! You Lose!')
            break
    else:
        if choice in ('even', 'e'):
            print(f'You {num} + {comp} Computer')
            print(f'{num + comp} is Odd, You Lose!')
            break
        else:
            print(f'You {num} + {comp} Computer')
            print(f'{num + comp} i  Odd, You Won!')
            woncount += 1

s = 'time' if woncount == 1 else 'times'
print('')
print(f'You won {woncount} {s}')
