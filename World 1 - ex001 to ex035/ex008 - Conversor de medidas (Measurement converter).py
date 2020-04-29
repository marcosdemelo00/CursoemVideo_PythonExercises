'''
Desafio 008:
Escreva um programa que leia um valor em metroe e o exiba convertido em
cintímetro e milímetros.
'''
m = float(input('Enter the length, in meters, that you want to covert: '))
print('{}m is equal to:\n{:.0f} centimeters and {:.0f} milimeters'.format(m, m*100, m*1000))