'''
Desafio 036:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário
ou então será negado.
'''
from time import sleep


# function to float validate
def isfloat(f):
    try:
        f = float(f)
        return True
    except:
        return False


# presentation and an input checker
print('Welcome to Loan simulator!\n')
sleep(1)
print('To know if you can take a Loan please inform:')
while True:
    total = input('Total loan value:\n > R$ ').strip()
    year = input('How many years do yo pretend to divide [1 to 30]:\n >    ').strip()
    salary = input('We need to know how much is your salary:\n > R$ ').strip()
    if isfloat(total) and float(total) > 0:
        total = float(total)
        if isfloat(salary) and float(salary) > 0:
            salary = float(salary)
            if year.isdigit() and 1 <= int(year) <= 30:
                year = int(year)
                break

    print('Error - Invalid values!')
    sleep(2)
    print('Please inform:')

# simulating a loading
count = 0
wait = 4
while True:
    print('Processing...')
    sleep(0.5)
    count += 0.5
    if count == wait:
        break
    print('Processing.')
    sleep(0.5)
    count += 0.5
    if count == wait:
        break
    print('Processing..')
    sleep(0.5)
    count += 0.5
    if count == wait:
        break

# solving problem
months = year * 12
if (total / months) > (salary * 0.30):
    print('\nThe installments would be R$ {:.2f} for {} months\n'
          'But sorry, we cannot offer you a loan!'.format((total / months), months))
else:
    print('\nThat\'s good, we can offer you a loan!\n'
          'The installments will be R$ {:.2f} for {} months'.format((total / months), months))
