'''
Desafio 033:
Faça um programa que leia três valores e mostre qual é o MAIOR e qual é o MENOR.
'''
while True:
    print('Enter three integers:')
    n1 = input('1 > ').strip()
    n2 = input('2 > ').strip()
    n3 = input('3 > ').strip()

    if n1.isdigit() and n2.isdigit() and n3.isdigit():
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        break
    else:
        continue
# Verifying the bigger:
if n1 > n2:
    if n1 > n3:
        print('The biggest value is:', n1)
    else:
        print('The biggest value is:', n3)
elif n2 > n3:
        print('The biggest value is:', n2)
else:
        print('The biggest value is:', n3)

# Verifying the lower:
if n1 < n2:
    if n1 < n3:
        print('The lowest value is', n1)
    else:
        print('The lowest value is', n3)
elif n2 < n3:
    print('The lowest value is', n2)
else:
    print('The lowest value is', n3)
