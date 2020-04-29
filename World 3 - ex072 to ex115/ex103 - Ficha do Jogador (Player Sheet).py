'''
Desafio 103:
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: o noe de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogados, mesmo que algum dado
não tenha sido informado corretamente.
'''


def sheet(name='<Unknown>', goals=0):
    print(f'Player {name} scored {goals} goals.')


n = input('Soccer player name: ').strip()
while True:
    g = input('Scored goals: ').strip()
    if g.isdigit() and int(g) >= 0:
        break
    else:
        g = 0
        break

if n == '':
    sheet(goals=g)
else:
    sheet(n, g)
