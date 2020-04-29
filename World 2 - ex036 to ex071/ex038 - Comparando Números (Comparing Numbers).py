'''
Desafio 038:
Escreva um programa que leia dois númeors inteiros e compare-os, mostrando na
tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

while True:
    print('Enter two integers:')
    n1 = input('Integer 1 > ').strip()
    n2 = input('Integer 2 > ').strip()
    if n1.isnumeric() and n2.isdigit():
        n1 = int(n1)
        n2 = int(n2)
        if n1 > n2:
            print('The first value is the greater.')
        elif n1 < n2:
            print('The second value is greater.')
        else:
            print('There is no greater value, both are equal.')
        break
    else:
        continue
