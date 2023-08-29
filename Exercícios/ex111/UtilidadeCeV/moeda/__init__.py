def aumentar(a=0, b=0, formatado=False):
    a = a + (a * b/100)
    if formatado:
        return f'R${a}'
    return a


def diminuir(a=0, b=0, formatado=False):
    a = a - (a * b/100)
    if formatado:
        return f'R${a}'
    return a


def dobro(a=0, formatado=False):
    a = a * 2
    if formatado:
        return f'R${a}'
    return a


def metade(a=0, formatado=False):
    a = a / 2
    if formatado:
        return f'R${a}'
    return a


def moeda(a=0, moeda = 'R$'):
    return f'{moeda}{a:.2f}'.replace('.', ',')


def resumo(v, p, pm):
    print('~'*15)
    print('RESUMO DO VALOR')
    print('~'*15)
    print(f'Preço analisado R${v}\nDobro do preço R${dobro(v)}\nMetade do preço R${metade(v)}\n{p}% de aumento R${aumentar(v, p)}\n{pm}% de redução R${diminuir(v, pm)}')