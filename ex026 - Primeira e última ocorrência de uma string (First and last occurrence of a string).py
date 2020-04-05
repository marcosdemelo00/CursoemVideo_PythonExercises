'''
Desafio 026:
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
'''

frase = input('That is you chance to tell something to anyone to anything!\n'
              'Please do the honors:\n > ').strip()
count = frase.count('a')
first = frase.find('a')
last = frase.rfind('a')
print('Look at this... your speech has {} \'a\'s,but this is not all...\n'
      'the first \'a\' is in the position {} \nand last at {}, cool isn\'t it?'
      .format(count, first + 1, last + 1))