'''
Desafio 032:
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
from datetime import date

y = input('What year do you want to know if it was or will be a Leap year?'
          '\n[Enter 0 to current year]\n> ').strip()

while True:
    if y.isdigit() and int(y) > 0:
        y = int(y)
        break
    elif int(y) == 0:
        y = date.today().year
        break
    else:
        y = input('Invalid year. Try again: \n> ').strip()

if (y // 100) % 4 == 0 or y % 400 == 0:
    print('{} is a Leap year.'.format(y))
else:
    print('{} is NOT a Leap year...'.format(y))