'''
Desafio 022:
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maúsculas
- O nome com todas minúsculas.
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome.
'''

name = input('Please, enter your full name: \n')
print('hello {}.'.format(name.upper()))
print('or do you prefer {}.'.format(name.lower()))
print('Did you know thar your name has {} letters? Of course without counting the spaces'
          .format(len(name) - name.count(' ')))
print('and in the casa that you do\'nt know your name has {} letters.'
          .format(name.find(' ')))
