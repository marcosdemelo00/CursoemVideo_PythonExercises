'''
Desafio 072:
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por
extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por
extenso.
'''

numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
           'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
           'sixteen', 'seventeen', 'elghteen', 'nineteen', 'twenty')
exit = False
while not exit:
    print('Enter a integer number from 0 to 20 and receive it in full.')
    while True:
        num = input('[0 to 20] ⇾  ')
        if num.isdigit() and int(num) in range(0, 21):
            num = int(num)
            print(f'{num} in full is {numbers[num].upper()}', end='\n')
            break

    while True:
        exit = input('Do you want to try again? [Y/N]')
        if exit in ('yes', 'y', ''):
            exit = False
            break
        elif exit in ('no', 'n'):
            exit = True
            break
