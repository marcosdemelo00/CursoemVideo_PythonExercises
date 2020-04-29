'''
Desafio 088:
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa
vai perguntar quantos jogos seráo gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep

print('\n' + '+-*/' * 7 + '+-*')
print(' Hunches Generator (MEGA SENA) ')
print('+-*/' * 7 + '+-*')

print()
while True:
    n = input('How many games do you want to generate?\n-> ').strip()
    if n.isdigit():
        n = int(n)
        break
    else:
        print('Invalid value, enter a integer number.')

hun = []
for x in range(0, n):
    hun.append([])
    for y in range(0, 6):
        while True:
            rand = randint(1, 60)
            if rand not in hun[x]:
                hun[x].append(rand)
                break
    hun[x].sort()

print()
print(f'>>>>>  RAFFLING {n} HUNCHES  <<<<<')
sleep(1.3)
for i in range(0, n):
    print(f'Hunch {i + 1:>{2}}: {hun[i]}')
    sleep(0.55)
print(f'>>>>>      GOOD LUCK!      <<<<<')
