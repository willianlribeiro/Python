somaidades = 0
homemvelho = 0
mediaidades = 0
nomehvelho = ''
mmenor = 0
for p in range(1, 5):
    print('---------{} Pessoa---------'.format(p))
    nome = str(input('Nome :')).strip()
    idade = int(input('Idade :'))
    sexo = str(input('Sexo [\033[34mM\033[m ou \033[31mF\033[m]')).strip()
    somaidades += idade
    if p == 1 and sexo in 'Mm':
        homemvelho = idade
        nomehvelho = nome
    if sexo in 'Mm' and idade > homemvelho:
        homemvelho = idade
        nomehvelho = nome
    if sexo in 'Ff' and idade <= 18:
        mmenor += 1
mediaidades = somaidades / 2
print('A média de todas as idades é de {}'.format(mediaidades))
print('O homem mais velho é {}, com {} anos de idade'.format(nomehvelho, homemvelho))
print('Existe(m) {} mulheres de menor nos dados informados'.format(mmenor))
