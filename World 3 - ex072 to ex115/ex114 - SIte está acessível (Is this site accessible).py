'''
Desafio 114:
Crie um código em Python que teste se o site Pudim está acessível pelo
computador usado.
'''

from urllib.request import urlopen


site = 'http://pudim.com.br/'
try:
    a = urlopen(site)
except:
    print('\n' + '-' * 40)
    print(f'I was not able to connect to {site}')
    print('-' * 40)
else:
    print('\n' + '-' * 40)
    print(f'I was able to successfully connect to {site}')
    print('-' * 40)
