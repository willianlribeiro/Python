numero = int(input('Coloque um número para saber a tabuada dele'))
for c in range(0, 11):
    print('{}x{}={}'.format(c, numero, c*numero))
    