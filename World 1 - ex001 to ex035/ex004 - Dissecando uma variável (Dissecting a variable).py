'''
Desafio 004:
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ele.
'''

val = input("Enter anything: ")
print("Value type is: ", type(val))
print('Only spaces? ', val.isspace())
print('Is it a number? ', val.isnumeric())
print('Is it alphabetic? ', val.isalpha())
print('Is it alphanumeric? ', val.isalnum())
print('Is it Uppercase? ', val.isupper())
print('Is it Lowercase? ', val.islower())
print('Is it Title? ', val.istitle())