'''
Desafio 019:
Um professor quer sortear um dos seus alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o
nome do escolhido.
'''

from random import choice
aluno1 = input('Qual o primeiro aluno: ')
aluno2 = input('Qual o segundo aluno: ')
aluno3 = input('Qual o terceiro aluno: ')
aluno4 = input('Qual o quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi {}'.format(choice(alunos)))

#ou

from random import choice
print('Digite o nome dos alunos, [para finalizar digite OK ]')
lista = []
test = ''
n = 1
while test != 'OK':
    add = input('Digite o nome do {}º aluno: '.format(n))
    if add == 'OK':
        break
    else:
        lista.append(add)
        n += 1
print(lista)
print('O aluno escolhido foi {}'.format(choice(lista)))
