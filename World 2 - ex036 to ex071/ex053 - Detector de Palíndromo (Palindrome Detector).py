'''
Desafio 053:
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
Ex.: apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
'''
print('-' * 49)
print('\033[31:40m  PALINDROME DETECTOR  \033[m | \033[7:31:40m'+'  PALINDROME DETECTOR  '[::-1]+'\033[m')
print('-' * 49 + '\n')

exit = False
while not exit:
    print('Enter a phrase or word and know if it is a PALINDROME:')
    phrase = input('> ').strip().upper()

    test = ''
    for l in phrase:
        if l.isalnum():
            test += l
        else:
            continue

    print('')
    if test == test[::-1]:
        print('\033[34m{}\033[m | \033[35m{}\033[m'.format(test, test[::-1]))
        print('{} is a \033[1:32mPALINDROME\033[m.'.format(phrase))
    else:
        print('\033[34m{}\033[m | \033[35m{}\033[m'.format(test, test[::-1]))
        print('{} is \033[1:31mnot a PALINDROME\033[m.'.format(phrase))

    end = input('\nWanna try again? [yes/no]').strip().lower()
    if end not in ['yes', 'y', '']:
        exit = True

