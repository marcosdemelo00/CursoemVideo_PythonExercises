'''
Desafio 023:
Faça um programa que lei um número de 0 a 9999 e mostre na tela cada um dos
dígitos separados.

Ex:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar; 1

'''

while True:
    num = input('Insert a number from 0 to 9999: ')
    if num.isnumeric() and int(num) >= 0 and int(num) <= 9999:
        break
#solving as string
v = len(num)

print('The number place value is: ')
v -= 1
uni = num[v]
print('Unit: {}'.format(uni))
if v > 0:
    v -= 1
    ten = num[v]
    print('Ten: {}'.format(ten))
    if v > 0:
        v -= 1
        hun = num[v]
        print('Hundred: {}'.format(hun))
        if v > 0:
            v -= 1
            tho = num[v]
            print('Thousand: {}\n'.format(tho))

#solving as number
num = int(num)
tho = num // 1000
hun = num // 100 % 10
ten = num // 10 % 10
uni = num // 1 % 10

print('The number place value is:\n'
      'Unit: {}\n'
      'Ten: {}\n'
      'Hundred: {}\n'
      'Thousand: {}'.format(uni, ten, hun, tho)
      )
