'''
Desafio 066:
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre eles.
(Desconsiderando o flag)
'''

def num():
    while True:
        try:
            n = float(input('Enter a number: [999 to stop] ').strip())
            return n
        except:
            print('Invalid value')


count = total = 0
while True:
    val = num()
    print(val)
    if val == 999:
        break
    else:
        count += 1
        total += val

print(f'{count} numbers was entered, their sum is {total}')
