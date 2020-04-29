'''
Desafio 035:
Desenvolva um program que leia o comprimento de três retas e diga ao usuário
se eles podem ou não formar um triângulo.
'''


def isfloat(f):
    try:
        float(f)
        return True
    except:
        return False


print('/' * 60)
print(f'{"   Triangle Analyzer   ":^60}')
print('\\' * 60)
print('\nI need you to tell me three measures.')
print('Then I can tell you if it\'s possible make a triangle.')
print('Now, Enter the triangle sides measures:')
while True:
    s1 = input('Side 1: > ').strip()
    s2 = input('Side 2: > ').strip()
    s3 = input('Side 3: > ').strip()
    tri = (s1, s2, s3)
    rep = True
    for i in tri:
        if isfloat(i) and float(i) > 0:
             rep = False
    if rep:
        print('Invalid values, try again:')
        continue
    else:
        s1, s2, s3 = float(s1), float(s2), float(s3)
        break

t1 = abs(s2 - s3) < s1 < (s2 + s3)
t2 = abs(s1 - s3) < s2 < (s1 + s3)
t3 = abs(s2 - s1) < s3 < (s2 + s1)
if t1 and t2 and t3:
    print('\n{}, {} and {} CAN form a triangle.'.format(s1, s2, s3))
else:
    print('\n{}, {} and {} CANNOT form a triangle'.format(s1, s2, s3))
