'''
Desafio 082:
Crie um programa que vai ler vários numeros e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e
os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

def num():
    while True:
        try:
            l.append(int(input('Enter a number: ').strip()))
            return repeat()
        except ValueError:
            print('Invalid Value.')


def repeat():
    while True:
        r = input('Continue? [Y/N] ').strip().lower()
        if r in ('yes', 'y', ''):
            return True
        elif r in ('no', 'n'):
            return False

l = []
cont = True
while cont:
    cont = num()

even = []
odd = []
for n in l:
    if n == 0:
        pass
    elif n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print(f'Full list: {l}')
print(f'Even values in list: {even}')
print(f'Odd values in list: {odd}')