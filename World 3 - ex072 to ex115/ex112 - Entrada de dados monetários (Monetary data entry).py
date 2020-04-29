'''
Desafio 112:
Dentro do pacote utilizades CeV que criamos no desafio 111, temos um módulo chamado
dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função
input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.
'''

from utilitiescev import data, currency

val = data.fnum('Enter a value: ')
currency.resume(val)