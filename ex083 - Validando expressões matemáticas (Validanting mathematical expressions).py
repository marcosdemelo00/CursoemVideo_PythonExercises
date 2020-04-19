'''
Desafio 083:
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses
abertos e fechados na ordem correta.
'''

print('''Enter a mathematical expression with parentheses
to know if it is a valid expression''')
exp = input(': ').strip()
test1 = test2 = True

for n in exp:
    if not n.isalnum() and n not in '%+-*/()!|π ':
        test1 = False
if exp.count('(') != exp.count(')'):
    test2 = False

if test1 == test2 == True:
    print('Valid Expression!')
else:
    if test2 == True:
        print('Invalid Expression, unknown/wrong symbol.')
    elif test1 == True:
        print('Invalid Expression, missing parentheses.')
    else:
        print('Invalid Expression, unknown/wrong symbol and missing parentheses.')
