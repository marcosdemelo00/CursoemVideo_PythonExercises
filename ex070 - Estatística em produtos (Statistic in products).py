'''
Desafio 070:
Crie um programa que leia o nome o o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1000.
c) Qual é o nome do produto mais barato.
'''

print('=' * 14)
print('  SHOP STORE  ')
print('=' * 14)

tot = expsv = cheap = cheapname = count = 0
exit = False
while not exit:
    print('-' * 14)
    prod = input('Product: ').strip()

    while True:
        try:
            price = float(input('Price: R$ ').strip())
            break
        except ValueError:
            continue

    print('-' * 14)

    if count == 0:
        cheapname = prod
        cheap = price
    elif cheap > price:
        cheapname = prod
        cheap = price
    count += 1
    tot += price
    if price >= 1000:
        expsv += 1

    while True:
        tobecont = input('Do you want to input another product? [Y/N]: ').strip().lower()
        if tobecont not in 'yn':
            continue
        elif tobecont == 'n':
            exit = True
        break

print('-' * 14 + '\n')
print(f'Total purchase price was R$ {tot:.2f}.')
print(f'From {count} products purchased, {expsv} cost most than R$ 1000.00 ')
print(f'{cheapname} is the cheapest product and it cost R$ {cheap:.2f}')
