'''
Desafio 109:
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um
parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado
pela função moeda(), desenvolvida no desafio 108.
'''

import ex109currency as ex109

val = ex109.floatnum()
print(f'Increasing 10% to {ex109.money(val)}: {ex109.increase(val, 10, True)}')
print(f'Decreasing 10% to {ex109.money(val)}: {ex109.decrease(val, 10, True)}')
print(f'Doubling R$ {ex109.money(val)}: {ex109.double(val, True)}')
print(f'Dividing in hal {ex109.money(val)}: {ex109.half(val, True)}')