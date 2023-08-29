def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Oops.. você não digitou um número inteiro válido')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar o valor')
            return 0
        else:
            return n


def linha(tam=40):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    listadep = []
    cabeçalho('Menu principal')
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print(linha())
    op = leiaInt('Opção:')
    return op


