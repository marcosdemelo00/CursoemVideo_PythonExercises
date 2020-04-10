'''
Desafio 040:
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÂO
- Média 7.0 ou superior: APROVADO
'''
def isfloat(f):
    try:
        f = float(f)
        return True
    except:
        return False


print('Enter the student grades:')
while True:
    n1 = input('1st > ').strip()
    n2 = input('2nd > ').strip()
    if isfloat(n1) and isfloat(n2):
        n1 = float(n1)
        n2 = float(n2)
        if n1 > 10 and n2 > 10:
            print('Grades must be between 0 and 10:')
            continue
        else:
            break
    else:
        continue

ave = (n1 + n2) / 2
if ave < 5:
    print('Your average was {:.2f}'.format(ave))
    print('DISAPPROVED')
    print('It wasn\'t this time...')
elif 5 <= ave < 7:
    print('Your average was {:.2f}'.format(ave))
    print('IN RECOVERY')
    print('You will have another chance, do your best!')
else:
    print('Your average was {:.2f}'.format(ave))
    print('APPROVED')
    print('Congratulations, continue with the good work!')