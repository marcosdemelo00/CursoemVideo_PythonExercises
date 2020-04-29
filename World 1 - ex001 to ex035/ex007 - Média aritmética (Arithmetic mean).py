'''
Desafio 007:
Desenvolva um program que leia as duas notas de um aluno, calcule e mostre a
sua média.
'''

while True:
    try:
        n1 = float(input('Enter the student\'s first grade: '))
        n2 = float(input('Enter the student\'s second grade: '))
        m = (n1 + n2) / 2
        print('The average student\'s grade in period is {:.1f}'.format(m))
        break
    except:
        print('Please, insert the grades correctly')


if m >= 7.00:
    print('Congratulation, you have reached the minimum grade')
else:
    print('Sorry, but you didn\'t reached the minimum grade')