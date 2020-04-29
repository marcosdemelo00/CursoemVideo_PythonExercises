'''
Desafio 085:
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente.
'''
def integ(v):
    while True:
        try:
            i = int(input(f'num{v} - ').strip())
            return i
        except:
            continue


print('_' * 20)
print('  The Seven Values  ')
print('_' * 20)

seven = [[],[]]
print('Enter 7 integer numbers:')
for n in range(1, 8):
    num = integ(n)
    if num % 2 == 0:
        seven[0].append(num)
    else:
        seven[1].append(num)
print()

seven[0].sort()
seven[1].sort()
if len(seven[0]) > 0:
    print(f'Even values:', end='')
    for i in seven[0]:
        print(f' [{i}]', end='')
else:
    print(f'No one even number.')
print()

if len(seven[1]) > 0:
    print(f'Odd values:', end='')
    for i in seven[1]:
        print(f' [{i}]', end='')
else:
    print(f'No one odd number')

print('\n\n', seven)