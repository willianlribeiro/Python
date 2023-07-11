print('Progressão aritimética')
i = int(input('Defina o início da PA'))
r = int(input('Escolha a razão da PA'))
decimo = i + (10 - 1) * r
for c in range(i, decimo, r):
    print('-{}'.format(c), end='-')
