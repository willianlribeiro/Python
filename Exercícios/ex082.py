lista = []
listap = []
listai = []
while True:
    numero = int(input('Digite aqui valor'))
    lista.append(numero)
    if numero % 2 == 0:
        listap.append(numero)
    else:
        listai.append(numero)
    r = str(input('Deseja continuar? S / N'))
    if r in 'Nn':
        break
print(f'A lista geral ficou assim: \n {lista}')
print(f'A lista dos números pares ficou assim: \n {listap}')
print(f'A lista dos números impares ficou assim: \n {listai}')
