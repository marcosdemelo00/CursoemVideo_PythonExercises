'''
Desafio 039:
Faça um program que leia o ano de nascimento de um jovem e informe, de acordo
com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deveerá mostrar o tempo que falta ou que passou do prazo
'''
from datetime import date

print('Military Enlistment informator!')
while True:
    birth = input('Enter you birth year:\n > ').strip()
    if birth.isdigit():
        birth = int(birth)
        break
    else:
        continue

year = date.today().year
month = date.today().month
age = year - birth
print('Who was born in {} is {} years old in {}.'.format(birth, age, year))
if age < 17:
    print('You will need to enlist in {} years and {} months'.format(18 - age, 12 - month))
elif age == 17:
    if month < 12:
        print('You will need to enlist in {} months'.format(12 - month))
    else:
        print('You will need to enlist next month')
elif age == 18:
    if month <= 4:
        print('It\'s time to enlist right now')
    elif month == 12:
        print('You missed the enlistment period this year, enlist in next month')
    else:
        print('You missed the enlistment period this year, enlist in {}'.format(12 - month))
else:
    if month <= 4:
        print('You are {} years and {} month late for your enlistment'.format(age - 19, 12 - month))
    elif month == 5:
        print('You are {} year late for your enlistment'.format(age - 18))
    else:
        print('You are {} years and {} month late for your enlistment'.format(age - 18, month - 4))
