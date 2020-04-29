'''
Desafio 017:
Faça um programa que leia o comprumento do cateto oposto e do cateto
abjacente de um triângulo retângulo, calcule e mostre o comprimento
da hipotenusa.
'''

print('Vamos calcular o valor da hipotenusa de um triangulo retângulo')
op = float(input('Qual o valor do Cateto Oposto? '))
ad = float(input('QUal o valor do Cateto adjacente? '))
print('A hipotenusa deste triangulo é {}'.format(((op**2)+(ad**2))**(1/2)))

from math import hypot as hipo
op = float(input('Qual o valor do Cateto Oposto? '))
ad = float(input('QUal o valor do Cateto Adjacente? '))
print('O valor da hipotenusa é {}'.format(hipo(op, ad)))