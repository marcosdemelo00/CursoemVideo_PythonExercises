'''
Desafio 015:
Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
print('Rented car!')
print('We\'re going to calculate how many you will pay for the car rental.')
days = int(input('For how many days did you rent the car?\n'))
km = float(input('And for how many kilometers did you drive the car?\n'))
print('You need to pay ${:.2f} for cars rental'.format((days*60) + (km*0.15)))