'''
Desafio 065:
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O
programa deve perguntar ao usuário se ele que ou não continuar a digitar valores.
'''
def rint(t):
    while True:
        try:
            i = int(input('{}'.format(t)).strip())
            return i
        except:
            print('It\'s not a integer.')


keep = 'yes'
total = count = big = small = 0

while keep in ('yes', 'y', ''):
    num = rint('Enter a integer: ')
    total += num
    if count == 0:
        big = small = num
    elif num > big:
        big = num
    elif num < small:
        small = num
    count += 1
    keep = input('Do you want to continue? [Yes/No]').strip().lower()

print('{} numbers was entered, their average is {:.2f}.'.format(count, total/count))
print('The biggest number was {} and the smallest was {}.'.format(big, small))
