'''
Desafio 043:
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40: Obesidade mórbida.
'''
def isfloat(f):
    try:
        f = float(f)
        return True
    except:
        return False

print('\033[1:35m)(\033[m' * 10)
print('  \033[1:35mB\033[mody \033[1:35mM\033[mass \033[1:35mI\033[mndex')
print('\033[1:35m)(\033[m' * 10)
print('\nEnter your height and weight:')
while True:
    height = input('height [m] > ').strip()
    weight = input('weight [Kg] > ').strip()
    if isfloat(height) and isfloat(weight):
        height = float(height)
        weight = float(weight)
        if height > 0 and weight > 0:
            break
        else:
            print('Negative or zero values are invalid.')
            continue
    else:
        print('Invalid values')
        continue

bmi = (weight/(height ** 2))
print('')
if bmi < 18.5:
    print('BMI = {:.1f} - You are \033[31mbelow normal weight\033[m, take care of yourself,'.format(bmi))
elif bmi < 25:
    print('BMI = {:.1f} - You are with a \033[32mnormal weight\033[m, \nkeep it up!'.format(bmi))
elif bmi < 30:
    print('BMI = {:.1f} - You are with \033[31moverweight\033[m, \ntake care of yourself, do exercises'.format(bmi))
elif bmi < 40:
    print('BMI = {:.1f} - You are with a \033[31mobesity degree\033[m, \nyou really need to take care of yourself, look for help.'.format(bmi))
else:
    print('BMI = {:.1f} - You are with \033[31mmorbid obesity\033[m, \nplease look for help, you are in real danger'.format(bmi))
