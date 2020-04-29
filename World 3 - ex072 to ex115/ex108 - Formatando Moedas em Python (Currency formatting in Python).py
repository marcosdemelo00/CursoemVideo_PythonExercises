'''
Desafio 108:
Adapte o código do desafio 107, criando uma função adicional chamada moeda() que
consiga mostrar os valores como um valor monetário formatado.
'''

import ex108currency as ex108

val = float(input('Enter value: R$ '))  #Resolve validation later
print(f'Increasing 10% to {ex108.money(val)}: {ex108.money(ex108.increase(val, 10))}')
print(f'Decreasing 10% to {ex108.money(val)}: {ex108.money(ex108.decrease(val, 10))}')
print(f'Doubling R$ {ex108.money(val)}: {ex108.money(ex108.double(val))}')
print(f'Dividing in hal {ex108.money(val)}: {ex108.money(ex108.half(val))}')