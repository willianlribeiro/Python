cor = ('\033[m',
       '\033[0;30;41m',
       '\033[0;30;42m',
       '\033[0;30;43m',
       '\033[0;30;44m',
       '\033[1;30;47m')


def titulo(msg):
    tam = len(msg) + 2
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)


def ajuda(comand):
    print(f'Acessando ajuda para -> {comand} <-')
    print(cor[5], end='')
    help(comand)
    print(cor[0], end='')


print(cor[3], end='')
titulo('Bem-vindo ao sistema de ajuda personalizado PYTHON')
print(cor[0], end='')
while True:
    resposta = input('Digite o comando:').lower().strip()
    if resposta == 'fim':
        break
    else:
        ajuda(resposta)
print(cor[1], end='')
titulo('Obrigado por utilizar meu programa.')
print(cor[0], end='')
