'''
Desafio 090:
Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final mostre o conteúdo da estrutura na tela.
'''
data = {}

print('\n STUDENT SITUATION \n')
print('Enter student informations:')
data['name'] = input('Name: ').strip()

while True:
    try:
        data['average'] = float(input(data['name'] + ' Average grade: ').strip())
        break
    except:
        continue

if data['average'] >= 7:
    data['situation'] = 'Approved'
elif 5 <= data['average'] < 7:
    data['situation'] = 'Retake Exam'
else:
    data['situation'] = 'Disapproved'

print('-' * 25)
print(f'Student name is {data["name"]}.')
print(f' - His average grade is {data["average"]}.')
print(f' - {data["name"]} situation is {data["situation"]}')
print('-' * 25)
print('\n', data)