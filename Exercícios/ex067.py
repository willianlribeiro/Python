while True:
    tabuada = int(input('Quer ver a tabuada de qual valor?'))
    print('-'*10)
    if tabuada < 0:
        break
    for n in range(11):
        valor = tabuada * n
        print(f'{tabuada}x{n} = {valor}')
    print('-'*10)
print('Você digitou um valor negativo. O programa terminou.')
