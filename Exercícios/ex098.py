from time import sleep


def contador(a, b, c):
    while True:
        if c == 0:
            c = 1
        if a == b:
            print('FIM!')
            break
        if b < a:
            print(a, end=' ')
            a -= c
            sleep(0.5)
        else:
            print(a, end=' ')
            a += c
            sleep(0.5)
print()


# Programa principal

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez. Digite a partir de qual número deseja começar e até qual quer ir')
inicio = int(input('Início'))
fim = int(input('Fim'))
passo = int(input('De quanto em quanto?'))
contador(inicio, fim, passo)
