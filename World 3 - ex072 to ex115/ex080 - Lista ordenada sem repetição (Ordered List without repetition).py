'''
Desafio 080:
Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o
sort()).
No final, mostre a lista ordenada na tela.
'''
mylist = []
for i in ('1st', '2nd', '3rd', '4th', '5th'):
    while True:
        try:
            val = int(input(f'Enter {i} value: ').strip())
            val2 = val
            break
        except ValueError:
            continue

    if mylist == []:
        mylist.append(val)
        print('Added at the list end.')
    else:
        for p, v in enumerate(mylist):
            if val > mylist[len(mylist) - 1]:
                mylist.append(val)
                print('Added at the list end.')
            elif val < v:
                mylist.insert(p, val)
                print(f'Added at the position {p}.')
                break

print(f'The entered numbers in order is {mylist}')
