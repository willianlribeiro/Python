def aumentar(a=0, b=0):
    a = a + (a * b/100)
    return a


def diminuir(a=0, b=0):
    a = a - (a * b/100)
    return a


def dobro(a=0):
    a = a * 2
    return a


def metade(a=0):
    a = a / 2
    return a


def moeda(a=0, moeda = 'R$'):
    return f'{moeda}{a:.2f}'.replace('.', ',')

