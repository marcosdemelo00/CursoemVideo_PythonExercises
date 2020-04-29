'''
Desafio 010:
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos Dólares ela pode comprar.
Considere US$1,00 = R$3,27
'''
c = float(input('How many Reais do you have in your pocket?\nR$ '))
print('With R$ {:.2f} you can buy: \n$ {:>7.2f}'.format(c, c / 3.27))