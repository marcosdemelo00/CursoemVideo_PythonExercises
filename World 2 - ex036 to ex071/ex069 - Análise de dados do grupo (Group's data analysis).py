'''
Desafio 069:
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
a) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados.
c) quantas mulheres tem menos de 20 anos.
'''

print('|Register|')
exit = False
age = man = woman = 0
while not exit:
    while True:
        y = input('Age: ').strip()
        if y.isdigit():
            y = int(y)
            break

    while True:
        s = input('Sex [M/F]: ').strip().lower()
        if s in 'mf':
            break

    if y >= 18:
        age += 1
    if s == 'm':
        man += 1
    if y >= 20 and s == 'f':
        woman += 1

    while True:
        out = input('Do you want to continue? [Y/N]: ').strip().lower()
        if out not in 'yn':
            continue
        elif out == 'n':
            exit = True
        break

print('')
print(f'{age} registered people are over 18.')
print(f'{man} men were registered.')
print(f'{woman} registered women are over 20.')