'''
Desafio 084:
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em
uma lista. No final mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem cem as pessoas mais pesadas.
c) Umalistagem ocm as pessoas mais leves.
'''
def weight():
    while True:
        try:
            a = float(input('Weight [Kg]: ').strip())
            if a > 0:
                return a
        except:
            continue

print('*' * 13)
print(' Weight List ')
print('*' * 13, end='\n')

data = []
temp = []
while True:
    temp.append(input('Name: ').strip())
    temp.append(weight())
    data.append(temp[:])
    temp.clear()
    exit = input('Continue: [Y/N]').strip().lower()
    if exit in ('n', 'no'):
        break

wmax = wmin = data[0][1]
nmax = []
nmin = []
for p in data:
    if p[1] > wmax:
        wmax = p[1]
        nmax = [p[0]]
    elif p[1] == wmax:
        nmax.append(p[0])

    if p[1] < wmin:
        wmin = p[1]
        nmin = [p[0]]
    elif p[1] == wmin:
        nmin.append(p[0])

print(f'{len(data)} people were registered')
print(f'Biggest weight was {wmax}. Weight of', end='')
for n in nmax:
    print(f' [{n}]', end='')
print(f'\nLowest weight was {wmin}. Weight of', end='')
for n in nmin:
    print(f' [{n}]', end='')
