lista = list()
banco = list()
maisp = maisl = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(int(input('Peso: ')))
    if len(banco) == 0:
        maisl = maisp = lista[1]
    else:
        if lista[1] > maisp:
            maisp = lista[1]
        if lista[1] < maisl:
            maisl = lista[1]
    banco.append(lista[:])
    lista.clear()
    r = str(input('Deseja continuar ? S  /  N'))
    if r in 'Nn':
        break
print(f'Foram cadastradas {len(banco)} pessoas')
print(f'Pessoas pesadas: {maisp}Kg =', end='')
for pc in banco:
    if pc[1] == maisp:
        print(f' {pc[0]}')
print(f'Pessoas leves: {maisl}Kg =', end='')
for pc in banco:
    if pc[1] == maisl:
        print(f' {pc[0]}')
