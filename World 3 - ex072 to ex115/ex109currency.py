def floatnum():
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