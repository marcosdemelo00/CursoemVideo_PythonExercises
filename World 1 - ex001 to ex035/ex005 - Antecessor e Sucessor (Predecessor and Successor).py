'''
Desafio 005:
Faça um programa qu eleia um número inteiro e mostre na tela o seu sucessor e
seu antecessor.
'''

while True:
    i = input('Enter a integer: ')
    try:
        i = int(i)
        break
    except:
        print('Try again!')

print(len(str(i)))
print('Successor of {} is: {:=^{leni}}!'.format(i, i + 1, leni=len(str(i))+4), end=' |  ')
print('Predecessor of {} is: >>>{}<<<!'.format(i, (i - 1)))