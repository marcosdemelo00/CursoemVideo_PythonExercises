'''
Desafio 012:
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com
5% de desconto.
'''
print('DISCOUNT CALCULATOR!')
p = float(input('Insert the product\'s price: \n$  '))
d = float(input('How many % os discount you get?\n'))
print('With {:.2f}% discount you will pay just \033[1m$ {:.2f}\033[0m.'.format(d, p * (1 - (d / 100))))
