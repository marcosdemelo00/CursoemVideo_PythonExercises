'''
Desafio 057:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
Caso esteja errado, peaça a digitação novamente até ter um valor correto.
'''

sex = 'X'
while not sex in 'MF':
    print('Enter you sex [M/F]:')
    sex = input('> ').strip().upper()[0]
    if not sex in 'MF':
        print('Invalid option.')

print('You are {}. Successfully registered!'.format('male' if sex == 'M' else 'female'))