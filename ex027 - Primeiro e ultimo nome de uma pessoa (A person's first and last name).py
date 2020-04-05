'''
Desafio 027:
Faça um programa que leia o nome completo de uma pessoa, mostrando em
seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''

name = input('Plese give me your full name... Again:\n').strip()
booom = name.split()
print('I know you know that but...\nYou first name is: {} '
      '\nand your last name is: {}'.format(booom[0],booom[-1]))
print('>', booom[0], booom[-1])
