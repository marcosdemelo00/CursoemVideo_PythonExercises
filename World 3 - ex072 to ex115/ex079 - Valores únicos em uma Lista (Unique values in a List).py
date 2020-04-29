'''
Desafio 079:
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''


l = []
while True:
    while True:
        n = input('Enter a integer number: ').strip()
        if n.isdigit():
            n = int(n)
            if n not in l:
                l.append(n)
                print('Number Added successfully.')
            else:
                print('This number has already been added.')
            break
        else:
            print('Invalid value.')
            continue

    repeat = input('Do you want to continue? [Y/N] ').strip().lower()
    if repeat in ('yes', 'y', ''):
        continue
    else:
        break

l.sort()
print(f'The added numbers were {l[0]}', end='')
for i in l[1:len(l) - 1]:
    print(f', {i}',end='')
print(f' and {l[len(l) - 1]}.')
