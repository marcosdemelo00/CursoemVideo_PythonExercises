'''
Desafio 075:
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.
'''

print('Enter four integers:')
tup = ()
for i in ('1st', '2nd', '3rd', '4th'):
    while True:
        val = input(f'{i} -> ')
        if val.isdigit():
            val = int(val)
            tup += val,
            break

if 9 in tup:
    print(f'a) Number 9 was entered {tup.count(9)} times.')
else:
    print(f'a) Number 9 was not entered.')

if 3 in tup:
    print(f'b) The first number 3 is in position {tup.index(3) + 1}.')
else:
    print(f'b) Number 3 was not entered.')

even = ''
for v in tup:
    if v % 2 == 0 and v != 0:
        even += ' ' + str(v)
if len(even) > 0:
    print(f'c) The entered even numbers are{even}.')
else:
    print(f'c) Even numbers were not entered.')