'''
Desafio 071:
Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
'''

print('ATM' * 6)
print('    ATM SIMULATOR    ')
print('ATM' * 6, end='\n')

print(' How much do you want to withdraw?')
while True:
    value = input(' > R$ ').strip()
    if value.isdigit():
        tot = value = total = int(value)
        break
    else:
        print('Invalid value! \nTry again:', end=' ')

print('-' * 35)
notetype = 50
notecount = 0
while True:
    if tot >= notetype:
        notecount = tot // notetype
        tot -= notecount * notetype
        print(f'{notecount} banknotes of R$ {notetype:.2f}')
    else:
        if notetype == 50:
            notetype = 20
        elif notetype == 20:
            notetype = 10
        elif notetype == 10:
            notetype = 1
        else:
            break

print('-' * 35)
fif = twe = ten = one = 0
if value // 50 > 0:
    fif = value // 50
    value -= (fif * 50)
    print(f'{fif} banknotes of R$ 50,00')
if value // 20 > 0:
    twe = value // 20
    value -= (twe * 20)
    print(f'{twe} banknotes of R$ 20,00')
if value // 10 > 0:
    ten = value // 10
    value -= (ten * 10)
    print(f'{ten} banknotes of R$ 10,00')
if value / 1 != 0:
    one = value // 1
    value -= (one * 1)
    print(f'{one} banknotes of R$ 1,00')

# Guanabara
print('-' * 35)
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
