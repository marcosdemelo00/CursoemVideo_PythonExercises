'''
Desafio 037:
Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 hexadecimal
'''

print('\033[7:34m>  Numeric Base Converter  <\033[m\n')

num = input('Enter a decimal integer for conversion: \nInteger > ').strip()
base = input('Now select the new base:\n1 - Binary\n2 - Octal\n3 - Hexadecimal\n\nBase > ').strip()

while True:
    if num.isdigit() and base.isdigit() and int(base) in [1, 2, 3]:
        num = int(num)
        base = int(base)
        if base == 1:
            print('{} in Binary is {}'.format(num, bin(num)[2:]))
        elif base == 2:
            print('{} in Octal is {:o}'.format(num, num))
        elif base == 3:
            print('{} in Hexadecimal is {:X}'.format(num, num))
        break
    else:
        print('Invalid values!\n\n Plese enter:')
        num = input('Integer > ').strip()
        base = input('1 - Binary\n2 - Octal\n3 - Hexadecimal\n\nBase > ').strip()
