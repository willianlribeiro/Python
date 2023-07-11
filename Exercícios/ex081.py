cont = 0
lista = []
cinco = ''
while True:
    lista.append(int(input('Digite um valor')))
    cont += 1
    r = str(input('Deseja continuar? S / N'))
    if r in 'Nn':
        break
lista.sort(reverse=True)
print(f'Foram digitados {cont} números')
print(f'A lista de valores digitados, de forma decrescente: \n{lista}')
if 5 in lista:
    print('O valor "5" foi encontrado na lista')
else:
    print('O valor "5" não foi encontrado na lista')

