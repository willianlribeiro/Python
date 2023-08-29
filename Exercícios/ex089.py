print('Digite o nome e as notas do aluno')
aluno = list()
boletim = list()
continuar = ''
while True:
    aluno.append(str(input('Nome:')).upper())
    aluno.append(int(input('Primeira nota:')))
    aluno.append(int(input('Segunda nota:')))
    continuar = str(input('Continuar?[S/N]'))
    media = (aluno[1] + aluno[2]) / 2
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()
    if continuar in 'nN':
        break
for i in range(0, len(boletim)):
    print(f'{i+1} ALUNO: {boletim[i][0]} MÉDIA {boletim[i][3]} ', end='')
    print()
while True:
    resposta = int(input('Mostrar as notas de qual aluno?'))-1
    print(f'As notas do {boletim[resposta][0]} foram {boletim[resposta][1]} e {boletim[resposta][2]}')
    contin = str(input('Ver outras notas ? [S/N]'))
    if contin in 'nN':
        break
print('Finished')