'''
Desafio 073:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da Chapecoence
'''

teams = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Athletico Paranaence', 'São Paulo',
         'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama',
         'Atlético', 'fluminence', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense',
         'Avaí')
print('-' * 15 + '\n\033[34mThe first five:\033[m')
for o, t in enumerate(teams[0:5]):
    if o == 0:
        oo = 'st'
    elif o == 1:
        oo = 'nd'
    elif o == 2:
        oo = 'rd'
    else:
        oo = 'th'
    print(f'{o + 1:>2}{oo} - {t}')
print('-' * 15 + '\n\033[33mThe last four:\033[m')
for o, t in enumerate(teams):
    if o >= len(teams) - 4:
        oo = 'th'
        print(f'{o + 1:>2}{oo} - {t}')
print('-' * 15 + '\n\033[31mIn alphabetic order:\033[m')
for t in sorted(teams):
    o = teams.index(t)
    if o == 0:
        oo = 'st'
    elif o == 1:
        oo = 'nd'
    elif o == 2:
        oo = 'rd'
    else:
        oo = 'th'
    print(f'{o + 1:>2}{oo} - {t}')
print('-' * 15 + '\n\033[32mChapecoense position:\033[m')
chape = teams.index('Chapecoense')
print(f'Chapecoence is in position {chape + 1}')
