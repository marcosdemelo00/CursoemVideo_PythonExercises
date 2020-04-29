'''
Desafio 098:
Faça um program que tenha uma função chamada contador(), que receba três parâmetros:
início, fim, e passo e realize a contagem.
'''
from time import sleep


def counter(ini, fin, stp):
    if stp == 0:
        stp = 1

    if ini <= fin:
        if stp < 0:
            print('Invalid Step!')
        else:
            for count in range(ini, fin + 1, stp):
                print(f'{count}', end=' ')
                sleep(0.3)
            print('Finish!')
    else:
        if stp > 0:
            stp *= -1
        for count in range(ini, fin - 1, stp):
            print(f'{count}', end=' ')
            sleep(0.3)
        print('Finish!')


print('MEGA BLASTER PLUS ADVANCED COUNTER')
sleep(0.7)
print('Counting from 1 to 10 in steps of 1')
sleep(0.7)
counter(1, 10, 1)
sleep(1.5)
print('Now, counting from 10 to 0 in steps of 2')
sleep(0.7)
counter(10, 0, 2)
sleep(0.7)
print('Try it yourself:')
while True:
    try:
        f = int(input('From: ').strip())
        l = int(input('To: ').strip())
        s = int(input('Step: ').strip())
        counter(f, l, s)
        break
    except:
        print('Error! Please insert just integer numbers.')