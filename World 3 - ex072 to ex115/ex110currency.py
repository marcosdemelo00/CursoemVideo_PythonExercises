def fnum():
    while True:
        try:
            v = float(input('Enter a value: ').strip().replace(',', '.'))
            return v
        except:
            print('Invalid value.')


def increase(val=0, tax=10, form=False):
    val += val * tax / 100
    return val if form is False else money(val)


def decrease(val=0, tax=10, form=False):
    val -= val * tax / 100
    return val if form is False else money(val)


def double(val=0, form=False):
    val = val * 2
    return val if form is False else money(val)


def half(val=0, form=False):
    val = val / 2
    return val if form is False else money(val)


def money(val=0, curr='R$'):
    return f'{curr} {val:.2f}'.replace('.', ',')


def resume(val=0, taxinc=10, taxdec=10):
    print('-' * 30)
    print('CURRENCY RESUME'.center(30))
    print('-' * 30)
    text = 'Analised Value: '
    print(f'{text}{money(val).rjust(30 - len(text))}')
    text = 'Double of Value:'
    print(f'{text}{double(val, True).rjust(30 - len(text))}') #or use \t
    text = 'Half of Value:'
    print(f'{text}{half(val, True).rjust(30 - len(text))}')
    text = f'{taxinc}% of increase: '
    print(f'{text}{increase(val, taxinc, True).rjust(30 - len(text))}')
    text = f'{taxdec}% of decrease: '
    print(f'{text}{decrease(val, taxdec, True).rjust(30 - len(text))}')
    print('-' * 30)
