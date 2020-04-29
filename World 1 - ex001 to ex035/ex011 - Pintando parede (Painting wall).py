'''
Desafio 011:
Faça um programa que leia a largura e a altura de uma parede em metros, calcule
a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
litro de tinta, pinta uma área de 2m².
'''
print('Let\'s calculate how many ink do you will need to paint a wall.')
w = float(input('Please, enter the wall\'s Width in meters: '))
h = float(input('Now enter the Height of the wall, in meters: '))
print('Considering that 1 liter of ink paints 2 square meters.')
print('You will need \033[1m {:.2f} liter\033[0m of ink to paint \033[1m{:.2f} square meters\033[0m of wall'. format(w * h / 2, w * h))