'''
Desafio 081:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
'''
def repeat():
    while True:
        cont = input('Continue? [Y/N] ').strip().lower()
        if cont in ('yes', 'y', ''):
            cont = True
        elif cont in ('no', 'n'):
            cont = False
        else:
            continue
        return cont


l = []
cont = True
while cont:
    try:
        l.append(int(input('Enter a number: ').strip()))
        cont = repeat()
    except ValueError:
        continue

print(f'You insert {len(l)} values.')
l.sort(reverse=True)
print(f'Values in decressed order: {l}')
if 5 in l:
    print('5 is on the list.')
else:
    print('5 is not on the list.')