from random import randint
from time import sleep
sorteados = []


def sorteio():
    for n in range(0, 5):
        sorteados.append(randint(0, 10))


def somaPar(lista):
    somadospares = 0
    for n in lista:
        if n % 2 == 0:
            somadospares += n
    print(somadospares)


sorteio()
print(sorteados)
sleep(0.3)
somaPar(sorteados)

