'''
Desafio 077:
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

words = ('interface', 'python', 'github', 'programing', 'data', 'computer', 'language',
         'tester', 'course', 'android', 'tuples')
y = '\033[33m'
n = '\033[m'
for w in words:
    print(f'The word {y}{w.upper()}{n} has ', end='')
    for l in w:
        if l.lower() in 'aeiou':
            print(f'{y}{l.upper()}{n} ', end='')
    print('as vowels.')