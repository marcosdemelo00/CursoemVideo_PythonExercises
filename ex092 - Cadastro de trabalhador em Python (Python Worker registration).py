'''
Desafio 092:
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente
de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa cai se aposentar.
'''
from datetime import datetime
def intval(v):
    while True:
        try:
            i = int(input(f'{v.capitalize()} : '))
            return i
        except:
            continue


year = datetime.now().year
data = {}
print('\n--- WORKER REGISTER ---\n')

print('Enter information:')
data['name'] = input('Name: ').strip()
while True:
    birth = intval('birth date')
    age = year - birth
    if age <= 0:
        print('Invalid value.')
    else:
        data['age'] = age
        break

while age >= 18:
    card = intval('work card [0 to blank]')
    if card <= 0:
        data['work card'] = 0
        break
    else:
        data['work card'] = card

    data['hiring year'] = intval('hiring year')
    data['salary'] = intval('salary')
    data['retirement'] = (data['hiring year'] - birth) + 35
    break

print('-=' * 25 + '\n', data)
for k, v in data.items():
    print(f'{k.capitalize()} has value: {v}.')
if data['age'] < 18:
    print('You are young cannot be registered!')
