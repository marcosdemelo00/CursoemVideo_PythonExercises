'''
Desafio 095:
Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um
sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
def goals(p):
    goalsgame = []
    while True:
        try:
            games = int(input(f'How many games did {p} played? ').strip())
            for i in range(0, games):
                while True:
                    try:
                        goalsgame.append(int(input(f'  How many goals in game '
                                                   f'{i + 1}? ').strip()))
                        break
                    except:
                        continue
            return goalsgame
        except:
            continue


def repeat():
    while True:
        exi = input('Continue? ').strip().lower()
        if exi in ('yes', 'y', ''):
            return True
        elif exi in ('no', 'n'):
            return False


dataset = []
player = {}

while True:
    player['name'] = input('Enter player name: ').strip()
    player['goals'] = goals(player['name'])
    player['total'] = len(player['goals'])
    dataset.append(player.copy())
    if not repeat():
        break
print('<>' * 19)
print(f' {"Id":<3} {"Name":<10} {"Goals":<15} {"Total"}')
print('<>' * 19)

for i, pl in enumerate(dataset):
    print(f' {i + 1:>3} {pl["name"]:<10} {pl["goals"]!s:<15}'
          f' {pl["total"]:>5}')
print('<>' * 19)

while True:
    try:
        more = int(input('Enter player Id for more information: [0 to finish] ')
                   .strip())
        if more <= 0:
            print('Finishing...\n\n')
            break
        elif more <= len(dataset):
            print(f' -- PLAYER {dataset[more - 1]["name"].upper()} INFORMATION:')
            for game, goals in enumerate(dataset[more - 1]['goals']):
                print(f'    In game {game + 1} scored {goals} goals.')
        else:
            print('Invalid Id.')
        print('<>' * 19)
    except:
        print('Invalid value.')

print('Thank you for using our product!')