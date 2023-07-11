print('Progressão aritimética')
i = int(input('Defina o início da PA'))
r = int(input('Escolha a razão da PA'))
cont = 1
termo = i
while cont <= 10:
    print('{}'.format(termo), end=' ')
    termo += r
    cont += 1
print('Cabou')