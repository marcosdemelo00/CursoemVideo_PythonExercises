'''
Desafio 041:
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mestre sua categoria, de acordo com a idade:
- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 25 anos: SÊNIOR
- Acima: MASTER
'''
from datetime import date

year = date.today().year
print('\033[1:32mAthlete Classification\033[m')
while True:
    birth = input('Enter your birth year: > ').strip()
    if birth.isdigit() and 1900 <= int(birth) <= year:
        birth = int(birth)
        break
    else:
        print('That is not a valid age.')
        continue

age = year - birth
if age <= 9:
    print('You are {} years old.\n Classification: CHILD ATHLETE'.format(age))
elif age <= 14:
    print('You are {} years old.\n Classification: INFANT ATHLETE'.format(age))
elif age <= 19:
    print('You are {} years old.\n Classification: JUNIOR ATHLETE'.format(age))
elif age <= 25:
    print('You are {} years old.\n Classification: SENIOR ATHLETE'.format(age))
else:
    print('You are {} years old.\n Classification: MASTER ATHLETE'.format(age))