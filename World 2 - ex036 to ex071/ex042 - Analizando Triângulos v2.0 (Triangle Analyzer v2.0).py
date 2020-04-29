'''
Desafio 042:
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
- Equilátero: todos os lado iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''

def isfloat(f):
    try:
        f = float(f)
        return True
    except:
        return False


print('-=-' * 10)
print('{:^62}'.format('\033[1:31mTRI\033[1:32mAN\033[1:34mGLE \033[1:30mANALYZER v2.0\033[m'))
print('-=-' * 10)
print('\nEnter three length and know if they can form a triangle:')

while True:
    s1 = input('lenght 1 > ').strip()
    s2 = input('lenght 2 > ').strip()
    s3 = input('lenght 3 > ').strip()
    if isfloat(s1) and isfloat(s2) and isfloat(s3):
        s1 = float(s1)
        s2 = float(s2)
        s3 = float(s3)
        if s1 > 0 and s2 > 0 and s3 > 0:
            break
        else:
            print('Negative or zero values are invalid, try again:')
            continue
    else:
        print('Invalid values, please try again:')
        continue

test1 = abs(s2 - s3) < s1 < s2 + s3
test2 = abs(s1 - s3) < s2 < s1 + s3
test3 = abs(s1 - s2) < s3 < s1 + s2
if test1 and test2 and test3:
    if s1 == s2:
        if s1 == s3:
            print('{}, {} and {} form a \033[32mEQUILATERAL TRIANGLE'.format(s1, s2, s3))
        else:
            print('{}, {} and {} form a \033[33mISOSCELES TRIANGLE'.format(s1, s2 ,s3))
    elif s1 == s3:
        print('{}, {} and {} form a \033[33mISOSCELES TRIANGLE'.format(s1, s2 ,s3))
    elif s2 == s3:
        print('{}, {} and {} form a \033[33mISOSCELES TRIANGLE'.format(s1, s2 ,s3))
    else:
        print('{}, {} and {} form a \033[34mSCALENE TRIANGLE'.format(s1, s2 ,s3))
else:
    print('{}, {} and {} can\'t form a \033[31mTRIANGLE'.format(s1, s2 ,s3))

#or

if test1 and test2 and test3:
    if s1 == s2 == s3:
        print('\033[m{}, {} and {} form a \033[32mEQUILATERAL TRIANGLE'.format(s1, s2, s3))
    elif s1 != s2 != s3 != s1:
        print('\033[m{}, {} and {} form a \033[34mSCALENE TRIANGLE'.format(s1, s2, s3))
    else:
        print('\033[m{}, {} and {} form a \033[33mISOSCELES TRIANGLE'.format(s1, s2, s3))
else:
    print('{}, {} and {} can\'t form a \033[31mTRIANGLE'.format(s1, s2 ,s3))