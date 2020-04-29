'''
Desafio 064:
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
'''

def isfloat(f):
    try:
        float(f)
        return True
    except:
        return False


num = count = total = 0
while num != 999:
    num = input('Enter a number [999 to stop]: ').strip()
    if isfloat(num):
        num = float(num)
    else:
        print('It is not a number!')
    if num != 999:
        count += 1
        total += num

print('You entered {} numbers and their sum is {}'.format(count, total))
