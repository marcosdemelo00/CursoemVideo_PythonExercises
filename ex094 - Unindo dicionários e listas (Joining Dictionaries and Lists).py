'''
Desafio 094:
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) A média de idade do grupo.
c) Uma lista com todas as mulheres.
d) Uma lista com todas as pessoas com idade acima da média.
'''
def repeat():
    while True:
        c = input('Continue? [Y/N] ').strip().lower()
        if c in ('yes', 'y', ''):
            return True
        elif c in ('no', 'n'):
            return False
        else:
            continue


data = {}
dataset = []
while True:
    data['name'] = input('Name: ').strip()
    while True:
        sex = input('Sex: [M/F] ').strip().lower()
        if sex == 'm':
            data['sex'] = 'male'
            break
        elif sex == 'f':
            data['sex'] = 'female'
            break
    while True:
        try:
            data['age'] = int(input('Age: ').strip())
            break
        except:
            continue
    dataset.append(data.copy())
    if not repeat():
        break

print(':=' * 20 + ':')
sum = count = 0
female = []

for reg in dataset:
    sum += reg['age']
    count += 1
    if reg['sex'] == 'female':
        female.append(reg['sex'])

print(f' Peoples registered: {len(dataset)}.')
print(f' Registered people have an average age of {sum / len(dataset):.1f}.')
print(f' Woman on registry: {female}.')
print(f' People with age above average:')
for p, d in enumerate(dataset):
    if d['age'] > (sum / count):
        print(f' - Name = {d["name"]}, Sex = {d["sex"]}, Age = {d["age"]}')