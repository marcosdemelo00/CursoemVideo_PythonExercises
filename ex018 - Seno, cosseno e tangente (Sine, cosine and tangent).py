'''
Desafio 018:
Faça um programa que leia um àngulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo.
'''


from math import radians, sin, cos, tan
ang = float(input('Digite o valor de um ângulo em grau centígrados: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sin(radians(ang))))
print('O ângulo de {} tem o CONSSENO de {:.2f}'.format(ang, cos(radians(ang))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan(radians(ang))))