def increase(val=0, tax=10):
    val += val * tax / 100
    return val


def decrease(val=0, tax=10):
    val -= val * tax / 100
    return val


def double(val=0):
    val = val * 2
    return val


def half(val=0):
    val = val / 2
    return val


def money(val=0, curr='R$'):
    return f'{curr} {val:.2f}'.replace('.', ',')