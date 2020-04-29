'''
Desafio 078:
Faça um programa que leia 5 valores numéricos e e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.
'''

lis = []
def val(i):
    try:
        f = input(f'{i} > ').strip()
        f = float(f)
        lis.append(f)
        return True
    except:
        return False


print('Enter 5 numbers:')
for i in ('1st', '2nd', '3rd', '4th', '5th'):
    exit = False
    while not exit:
        exit = val(i)


print(f'The higher value entered was {max(lis)} in position ', end='')
for i, v in enumerate(lis):
    if v == max(lis):
        print(f'{i + 1}... ', end='')
print('')
print(f'The lower value entered was {min(lis)} in position ', end='')
for i, v in enumerate(lis):
    if v == min(lis):
        print(f'{i + 1}...', end='')
