print('Progressão aritimética')
i = int(input('Defina o início da PA'))
r = int(input('Escolha a razão da PA'))
cont = 1
termo = i
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' ')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos gostaria de ver mais?'))
print('Finalizado com {} termos mostrados!'.format(cont - 1))


