'''
Desafio 105:
Faça um programa que tenha uma função notas() que pode receber várias notas de
alunos e vai retornar um dicionário com as seguintes informações:
 - Quantidade de notas
 - A maior nota
 - A menor nota
 - A média da turma
 - A situação (opcional)
Adicione também as docstrings da função.
'''
from statistics import mean


def grades(*n, sit=False):
    '''
    Function to analyse a lot of students grades and the situation of them.
    :param n: Students grades.
    :param sit: (Optional) Show or don't students situation.
    :return: Dictionary with class informations.
    '''
    info = dict()
    info['total'] = len(n)
    info['bigger'] = max(n)
    info['lower'] = min(n)
    info['average'] = round(mean(n), 2)
    if sit:
        if mean(n) >= 7:
            info['situation'] = 'Good'
        else:
            info['situation'] = 'Bad'
    return info


print(grades(7, 9, 5, 4, 10, sit=True))
help(grades)