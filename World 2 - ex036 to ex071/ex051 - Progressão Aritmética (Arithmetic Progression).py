'''
Desafio 051:
Desenvolva um programa que leia o primeiro termo e a razão de um PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

print('First 10 terms of an Arithmetic Progression.')
exit = False
while not exit:
    try:
        first = float(input('Enter the first term: ').strip())
        rate = float(input('Enter the difference: ').strip())
        total = 0
        for c in range(0,10):
            print('{:.1f}'.format(first + (rate * c)),end=' → ')
            total += first + (rate * c)
        print('It\'s over.')
        print('The AP sum is: {:.1f}'.format(total))
        finish = input('\nWanna try again? [yes/no]: ').strip().lower()
        if finish in ('yes', 'y', ''):
            continue
        else:
            exit = True
    except:
        print('Invalid value!')
