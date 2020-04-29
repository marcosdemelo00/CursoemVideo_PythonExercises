'''
Desafio 107:
Crie um módulo  moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
import ex107currency

val = float(input('Enter value: R$ '))  #Resolve validation later
print(f'Increasing 10% to R$ {val}: R$ {ex107currency.increase(val, 10)}')
print(f'Decreasing 10% to R$ {val}: R$ {ex107currency.decrease(val, 10)}')
print(f'Doubling R$ R$ {val}: R$ {ex107currency.double(val)}')
print(f'Dividing in hal R$ {val}: R$ {ex107currency.half(val)}')