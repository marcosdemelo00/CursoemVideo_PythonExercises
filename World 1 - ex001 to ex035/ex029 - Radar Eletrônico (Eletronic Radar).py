'''
Desafio 029:
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
'''

def isfloat (f):
    try:
        float(f)
        return True
    except:
        return False


spd = input('Enter car speed [Km/h]: ').strip()

while True:
    if isfloat(spd) and float(spd) >= 0:
        if float(spd) > 80:
            print('You were fined!\nThe fine will cost R$ {:.2f}.'.format((float(spd) - 80) * 7))
            spd = input('Enter a new value or type "End" to finish.\n> ').strip()
        else:
            print('It\'s everything Ok. You can go.')
            spd = input('Enter a new value or type "End" to finish.\n> ').strip()
    else:
        print('Please, enter a valid car speed [Km/h]:')
        spd = input('Enter a new value or type "End" to finish.\n>').strip()
    if spd.lower().strip() == 'end':
        break
print('Thanks for using our services!')