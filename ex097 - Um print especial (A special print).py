'''
Desafio 097:
Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá,Mundo!')

Saída:
~~~~~~~~~~~~
 Olá,Mundo!
~~~~~~~~~~~~
'''


def charmprint(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}  ')
    print('~' * (len(txt) + 4))


txt = input('Enter any phrase: \n> ')
charmprint(txt)