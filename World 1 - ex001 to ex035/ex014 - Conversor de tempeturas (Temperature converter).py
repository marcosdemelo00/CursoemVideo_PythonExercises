'''
Desafio 014:
Escreva um programa que converta uma temperatura digitada em ºC e converta para
ºF.
'''

options = ('1', '2', '3', 'Kelvin', 'Celsius', 'Fahrenheit')

print('TEMPERATURE CONVERTER!')
print('1 - Kelvin;\n2 - Celsius;\n3 - Fahrenheit.\nChoose the temperature scale that you want to convert: ', end='')
while True:
    type1 = input()
    if type1 not in options:
        print('Enter a valid option. Try again: ', end='')
    else:
        break

print('Enter the temperature you want to convert: ', end='')
while True:
    try:
        temp = float(input())
        break
    except:
        print('Insert a valid temperature: ', end='')


print('1 - Kelvin;\n2 - Celsius;\n3 - Fahrenheit.\nChoose what temperature scale you want to know: ', end='')
while True:
    type2 = input()
    if type2 not in options:
        print('Enter a valid option. Try again: ', end='')
#    elif type2 == type1:
#        print('You\'are trying to convert to same scale, please insert a different option: ', end='')
    else:
        break


if (type1 == '1' or type1 == 'Kelvin') and (type2 == '2' or type2 == 'Celsius'):
    print('{:.2f}K is equal to {:.2f}ºC'.format(temp, temp - 273))
elif (type1 == '1' or type1 == 'Kelvin') and (type2 == '3' or type2 == 'Fahrenheit'):
    print('{:.2f}K is equal to {:.2f}ºF'.format(temp, ((9*(temp - 273)/5)+32)))
elif (type1 == '2' or type1 == 'Celsius') and (type2 == '1' or type2 == 'Kelvin'):
    print('{:.2f}ºC is equal to {:.2f}K'.format(temp, temp + 273))
elif (type1 == '2' or type1 == 'Celsius') and (type2 == '3' or type2 == 'Fahrenheit'):
    print('{:.2f}ºC is equal to {:.2f}ºF'.format(temp, 1.8*temp + 32))
elif (type1 == '3' or type1 == 'Fahrenheit') and (type2 == '1' or type2 == 'Kelvin'):
    print('{:.2f}ºF is equal to {:.2f}K'.format(temp, ((5*(temp - 32)/9)+273)))
elif (type1 == '3' or type1 == 'Fahrenheit') and (type2 == '2' or type2 == 'Celsius'):
    print('{:.2f}ºF is equal to {:.2f}ºC'.format(temp, (temp - 32)/1.8))
else:
    if type1 == '1' or 'Kelvin':
        print('{:.2f}K is equal to {:.2f}K'.format(temp, temp))
    elif type2 == '2' or 'Celsius':
        print('{:.2f}ºC is equal to {:.2f}ºC'.format(temp, temp))
    elif type1 == '3' or 'Fahrenheit':
        print('{:.2f}ºF is equal to {:.2f}ºF'.format(temp, temp))