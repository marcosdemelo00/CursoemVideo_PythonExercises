'''
Desafio 076:
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
preços, na sequência.
No final, mostre uma lestagem de preços organizando os dados em forma tabular.
'''

smart = ('Xiaomi Mi 9T pro', 3339.42, 'Sansung Galaxy S10e', 2399.90, 'Sansung Galaxy S9',
         1789.00, 'Motorola One Vision', 1419.00, 'Sansung Galaxy A50', 1573.95,
         'Xiaomi Redmi Note 8', 1299.00, 'Motorola One Action', 1224.55, 'Zenfone Max Shot',
         891.65, 'Sansung Galaxy A20s', 829.90, 'Moto G8 Play', 829.00)

print('-' * 40)
print('{:^40}'.format('PRICE LIST'))
print('-' * 40)
for i in range(0,len(smart),2):
    print(f' {smart[i]:.<27} R$ {smart[i + 1]:>7.2f} ')
print('-' * 40)