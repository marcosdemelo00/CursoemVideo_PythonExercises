while True:
    n = float(input('Insert any number: '))
    print('{:.2f} is twice {:.2f}'.format(n * 2, n))
    print('{:.2f} is the triple of {:.2f}'. format(n * 3, n))
    print('{:.2f} is the square of {:.2f}'. format(n ** (1/2), n))