'''
Desafio 101:
Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''
from datetime import datetime


def vote(age):
    if age >= 70 or age in range(16, 18):
        vote = 'OPTIONAL VOTE'
    elif age < 16:
        vote = 'DO NOT VOTE'
    else:
        vote = 'COMPULSORY VOTE'
    print(f'With {age} years: {vote}.')

while True:
    year = input('Enter your birth year: ').strip()
    if year.isdigit():
        year = int(year)
        today = datetime.today().year
        age = today - year
        if age < 0:
            print('Invalid year.')
            continue
        break
    else:
        print('Invalid value, try again!')

vote(age)
