'''
Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
No final do pragrama, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''
count = 0
totalagef = 0
totalagem = 0
girlscount = 0
oldmanage = 0
for i in ('1st', '2nd', '3rd', '4th'):
    count += 1  # Just to insert more loops
    while True:
        print('----- {} person -----'.format(i))
        name = input('Name: ').strip().split()
        name = name[0]

        try:
            age = int(input('Age: ').strip())
        except:
            print('Invalid value!')
            continue

        sex = input('Sex [M/F]: ').strip().upper()
        if sex == 'F':
            totalagef += age
            if age < 20:
                girlscount += 1
            break
        elif sex == 'M':
            totalagem += age
            if age > oldmanage:
                oldmanage = age
                oldmanname = name
            break
        else:
            print('Invalid value!')
            continue

print('The avarege of persons age is {:.2f}.'.format((totalagef + totalagem)/count))
if totalagem > 0:
    print('The elder man is {}, he is {} years old.'.format(oldmanname, oldmanage))
print('There are {} girls with less than 20 years.'.format(girlscount))