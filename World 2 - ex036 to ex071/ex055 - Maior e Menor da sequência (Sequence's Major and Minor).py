'''
Desafio 055:
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o
maior e o menor peso lidos.
'''
print('Enter the weight (in Kg) of 5 persons:')

heavy = [0, '']
light = [0, '']
for i in ('1st', '2nd', '3rd', '4th', '5th'):
    while True:
        try:
            weight = float(input('{} person weight (Kg): '.format(i)).strip())
            break
        except:
            print('\nInvalid Value!')

    if weight > heavy[0]:
        heavy[0] = weight
        heavy[1] = i
    elif weight < light[0] or light[0] == 0:
        light[0] = weight
        light[1] = i


print('The heavier is the {} person with {} Kg'.format(heavy[1], heavy[0]))
print('The lighter is the {} person with {} kg'.format(light[1], light[0]))