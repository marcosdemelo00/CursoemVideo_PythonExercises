'''
Desafio 046:
Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from emoji import emojize
from time import sleep

#:fireworks: :sparkler: :clock12:
print('It\'s the \033[1:4:33mFINAL\033[m', end=' ')
print('\033[1:4:31mCOUNTDOWN\033[m!!!')
sleep(0.5)
for c in range(10, 0, -1):
    print(c)
    sleep(1)

f = emojize(':fireworks:', use_aliases=True)
s = emojize(':sparkler:', use_aliases=True)
h = emojize(':clock12:', use_aliases=True)
y = '\033[33m'
r = '\033[31m'
n = '\033[m'
print('\n{}{} BUM! {}{} {}{}{} BUUUUM! {}{} {}{}{} POOOOOW {}{}{}'.format(r,f,y,f,r,s,y,r,s,y,f,r,y,f,n))
print('0 !! {}{} Happy {}new year!!! {}{}'.format(h,r,y,n,h))
print('{}{} BUM! {}{} {}{}{} BUUUUM! {}{} {}{}{} POOOOOW {}{}{}'.format(r,f,y,f,r,s,y,r,s,y,f,r,y,f,n))