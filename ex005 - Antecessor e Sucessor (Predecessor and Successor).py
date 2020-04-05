while True:
    i = input('Digite um numero inteiro: ')
    try:
        i = int(i)
        break
    except:
        print('Tente novamente!')

print(len(str(i)))
print('O sucessor de {} é: {:=^{leni}}!'.format(i, i + 1, leni=len(str(i))+4), end=' |  ')
print('O antecessor de {} é: >>>{}<<<!'.format(i, (i - 1)))