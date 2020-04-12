'''
Desafio 054:
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
21 anos
'''
from datetime import date

today = date.today().year
major = 0
minor = 0
print('Enter the birth year of seven people:')

for c in ('1st', '2nd', '3rd', '4th', '5th', '6th', '7th'):
    while True:
        try:
            v = int(input('{} person:'.format(c)).strip())
        except:
            print('Invalid Value')
            continue

        if v >= 1900 and v <= today:
            if today - v <= 21:
                minor += 1
            else:
                major += 1
            break
        else:
            print('Invalid Value')
            continue

print('There are {} adults and {} minors.'.format(major, minor))