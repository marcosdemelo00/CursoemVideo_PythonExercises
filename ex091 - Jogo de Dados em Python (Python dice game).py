'''
Desafio 091:
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem
Sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

dice = {}
ranking = list()

print('Rolling dices...')
sleep(1)
for p in range(1, 5):
    dice['player' + str(p)] = randint(1, 6)
    print(f'Player{p} got {dice["player" + str(p)]}')
    sleep(0.5)

ranking = sorted(dice.items(), key=itemgetter(1), reverse=True) # return List
print('== Player Ranking ==')
for p, d in enumerate(ranking):
    if p == 0:
        ordi = 'st'
    elif p == 1:
        ordi = 'nd'
    elif p == 2:
        ordi = 'rd'
    else:
        ordi = 'th'
    print(f'{p + 1}{ordi} - {d[0]} {d[1]}')