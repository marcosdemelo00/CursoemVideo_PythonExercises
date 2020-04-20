'''
Desafio 089:
Crie um programa qu leia nome e duas notas de vários alunos e guarde tudo em uma
lista composta. No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.
'''
def repeat():
    while True:
        cont = input('Continue? [Y/N] ').strip().lower()
        if cont in ('yes', 'y', ''):
            return False
        elif cont in ('no', 'n'):
            return True
        else:
            continue


def note():
    while True:
        try:
            notes = []
            notes.append(float(input('1st Note: ').strip()))
            notes.append(float(input('2nd Note: ').strip()))
            return notes
        except:
            continue


data = []
exit0 = False


print('\n' + '=' * 19)
print('   NOTE REGISTER   ')
print('=' * 19 + '\n')

while not exit0:
    data.append([])
    data[len(data) - 1].append(input('Name: ').strip())
    data[len(data) - 1].append(note())
    exit0 = repeat()


print('\n' + '-' * 35 )
print('{:<3}| {:<10}| {:<5}| {:<10}'.format('Id', 'Name', 'Mean', 'Situation'))
print('-' * 35)
for p, d in enumerate(data):
    mean = (d[1][0] + d[1][1]) / 2
    print(f'{p:<3}| {d[0]:<10}| {mean:^5.1f}', end='')
    if mean >= 7:
        print(f'| {"Approved":<12}')
    else:
        print(f'| {"Disapproved":<12}')
print('-' * 35)

exit0 = False
while not exit0:
    while True:
        Id = input('Enter STUDENT Id for grades: ').strip()
        if Id.isdigit():
            Id = int(Id)
            if 0 <= Id <= (len(data) - 1):
                break
        print('Invalid Id. Try again.\n')

    print('-' * 35)
    print(f'Id:{Id:>3}| {data[Id][0]}| Grades:{data[Id][1]}')
    print('-' * 35)
    exit0 = repeat()

print('FINISHING...\n<<< COME BACK AGAIN >>>')