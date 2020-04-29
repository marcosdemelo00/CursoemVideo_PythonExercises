def increase(val, inc=10):
    val += val * inc / 100
    return val


def decrease(val, dec=10):
    val -= val * dec / 100
    return val


def double(val):
    val = val * 2
    return val


def half(val):
    val = val / 2
    return val