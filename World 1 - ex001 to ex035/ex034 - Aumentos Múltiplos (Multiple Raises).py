'''
Desafio 034:
Escreva um program que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores e iguais, o aumento é de 15%.
'''

def isfloat (f):
    try:
        float(f)
        return True
    except:
        return False


print('Hello, I\'m your Salary Increase calculator!')
print('All you need to do is inform the salary and I will show to you the new salary.')
sal = input('Enter the current salary: R$ ').strip()
while True:
    if isfloat(sal) and float(sal) >= 0:
        sal = float(sal)
        break
    else:
        sal = input('Enter a valid value: R$ ').strip()


if sal > 1250.00:
    sal += sal * 0.10
    print('The new salary will be: {:.2f}'.format(sal))
else:
    sal += sal * 0.15
    print('The new salary will be: {:.2f}'.format(sal))