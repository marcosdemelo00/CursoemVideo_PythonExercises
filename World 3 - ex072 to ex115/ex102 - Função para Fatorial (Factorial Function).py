'''
Desafio 102:
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o
primeiro que indique o número a calcular e o outro chamado show que será um valor
lógico (opcional) indicando se sera mostrado ou não na tela o processo de cálculo
fatorial.
'''


def factorial(num, show=False):
    """
    Calculates the factorial of a integer number. You can choose to receive the calculation process or don't.

    If value of 'num' was not an integer there will be a ValueError.

    :param num: Number to be calculated.
    :param show: (optional) Show or don't the calculation process.
    :return: Factorial of a integer number num.
    """
    num = int(num)
    fact = 1
    for v in range(num, 0, -1):
        fact *= v
        if show:
            print(f'{v}', end='')
            print(' * ' if v != 1 else ' = ', end='')
    return fact

print(factorial(5, True))
help(factorial)