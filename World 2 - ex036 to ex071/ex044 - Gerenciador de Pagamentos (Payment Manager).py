'''
Desafio 044:
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
from time import sleep


def isfloat(f):
    try:
        f = float(f)
        return True
    except:
        return False

exit = False
total = 0

while not exit:
    while True:
        print('Enter product value: [0 to exit]')
        value = input('R$ ').strip()
        if isfloat(value) and float(value) > 0:
            value = float(value)
            sleep(1)
            break
        elif isfloat(value) and float(value) == 0:
            exit = True
            break
        else:
            sleep(1)
            print('Invalid value!\n')
            sleep(1)
            continue

    while not exit:
        print('R$ {:.2f}'.format(value))
        print('''Enter a Payment Method:
        [1] Cash/Check
        [2] Cash Card
        [3] 2x Credit Card
        [4] 3x or more Credit Card
        [5] Return''')
        method = input(' > ').strip()
        if method in ['1', '2', '3', '5']:
            method = int(method)
            sleep(1)
            break
        elif method == '4':
            method = int(method)
            while True:
                parcel = input('How many time do you want to parcel?\n> ').strip()
                if parcel.isdigit():
                    parcel = int(parcel)
                    sleep(1)
                    break
                else:
                    sleep(1)
                    print('Invalid Value!\n')
                    sleep(1)
                    continue
            sleep(1)
            break
        else:
            sleep(1)
            print('Invalid Value!\n')
            sleep(1)
            continue

    try:
        if method == 1:
            value = value - (value * 0.1)
            print('Product will be paid as Cash/Check')
            print('That will cost R$ {:.2f}'.format(value))
        elif method == 2 or parcel == 1:
            value = value - (value * 0.05)
            print('Product will de paid as Cash Card')
            print('That will cost R$ {:.2f}'.format(value))
        elif method == 3 or parcel == 2:
            print('Product will de paid as 2x Credit Card')
            print('That will cost {} in 2x R$ {:.2f}'.format(value, value / 2))
        elif method == 4:
            value = (value + (value * 0.2))
            print('Product will be paid as {}x Credit Card'.format(parcel))
            print('That will cost {:.2f} in {}x R$ {:.2f}'.format(value, parcel, value / parcel))
        elif method == 5:
            continue
        sleep(2)
    except:
        exit = True

    while not exit:
        total += value
        rep = input('Want to add another payment? [yes/no]\n >')
        if rep == 'no' or rep == 'n':
            sleep(1)
            exit = True
            break
        elif rep == 'yes' or rep == 'y' or rep == '':
            print('')
            break
        else:
            sleep(1)
            print('Invalid value!\n')
            sleep(1)


print('\n\nThanks for choosing us!')
if total > 0:
    print('Total purchase was R$ {:.2f}'.format(total))
    print('Come again!')
else:
    print('Come again!')