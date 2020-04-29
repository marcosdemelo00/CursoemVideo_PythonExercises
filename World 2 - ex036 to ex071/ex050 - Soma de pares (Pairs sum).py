'''
Desafio 050:
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for ímpar desconsidere-o.
'''

print('Enter six Integers:')
total = 0
count = 0
even = ''
for n in range(1, 7):
    while True:
        try:
            num = input('Integer {} > '.format(n)).strip()
            num = int(num)
            break
        except:
            print('Invalid value!')
            continue

    if num % 2 == 0 and num > 0:
        total += num
        count += 1
        even += str(num) + ' '


print('')
print('There are {} even values, they are: {}.'.format(count, even[:len(even)-1]))
print('Their sum is: {}.'.format(total))
