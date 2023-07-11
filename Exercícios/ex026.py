frase = str(input('Coloque aqui uma frase aleatória')).lower().strip()
print('A letra "a" aparece {} vezes'.format(frase.count('a')))
print('A letra "a" aparece na posição {} a primeira vez'.format(frase.find('a')+1))
print('A letra "a" aparece na posição {} pela última vez'.format(frase.rfind('a')+1))