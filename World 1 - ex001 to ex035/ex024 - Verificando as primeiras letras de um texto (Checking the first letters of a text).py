'''
Desafio 024:
Crei um programa que leia o nome de uma cidade e diga se ela começa ou não com
o nome "SANTO".
'''

city = input('Please inform the name of the city that you live:\n')
city.lstrip()
if city[0:5].lower() == 'santo':
    print('The name of your city starts with "Santo"!')
else:
    print('The name of your city don\'t starts with "Santo"...')