'''
Desafio 093:
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
'''
def integ(t):
    if t.isdigit() and int(t) >= 0:
        return True
    else:
        return False

def line():
    print('<>' * 20)

data = {}
goals = []

data['name'] = input('Enter Player name: ').strip()
while True:
    game = input(f'How many games did {data["name"]} played? ')
    if integ(game):
        game = int(game)
        break

for i in range(0, game):
    while True:
        goal = input(f'    How many goals in game {i + 1}? ')
        if integ(goal):
            goals.append(int(goal))
            break

data['goals'] = goals
data['total'] = game

line()
print(data)
line()
for k, v in data.items():
    print(f'The key {k} has the value {v}.')
line()
print(f'The player {data["name"]} played {data["total"]} games.')
for i in range(0, game):
    print(f'    => In game {i + 1}, scored {data["goals"][i]} goals.')
line()