def fatorial(n, show=False):
    """
    Fatorial de algum número
    :param n: Número a ser fatorado
    :param show: Se deseja mostrar ou não o calculo
    :return: Retorna o valor do calculo
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print( c, end='')
            if c > 1:
                print(f' x ', end=' ')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa principal
print(fatorial(5, show=False))
