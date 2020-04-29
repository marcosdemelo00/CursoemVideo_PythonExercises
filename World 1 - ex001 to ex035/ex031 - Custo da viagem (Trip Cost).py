'''
Desafio 031:
Desenvolva um programa que perugnte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km
e R$ 0,45 para viagens mais longas.
'''

print('Hello! We are really happy that you chose our company.')
long = input('Now, please, tell me how far you trip will be: \n> ').strip()
while True:
    if not long.isdigit():
        print('Sorry, but that is not a valid distance [Just integers]:')
        long = input('> ').strip()
    elif int(long) <= 0:
        print('Sorry, but that is not a valid distance.')
        long = input('> ').strip()
    elif int(long) <= 200:
        print('Your travel has {} Km. \nAnd will cost R$ {:.2f}'.format(long, int(long)*0.5))
        break
    else:
        print('Your travel has {} Km. \nAnd will cost R$ {:.2f}'.format(long, int(long)*0.45))
        break

print('Be wellcome again! We wait your return.')
