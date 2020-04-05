'''
Desafio 025:
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

name = input('I need that you insert your full name NOW !! please:\n')
test = (name.lower().split())

if 'silva' in test:
    print('Soo... You are one of THEM... You are a Silva.')
else:
    print('Oh, that\'s new... You are not a Silva.')