from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *


arq = 'willproject.txt'
if not verificarArquivo(arq):
    criarArquivo('willproject.txt')

while True:
    op = menu(['Cadastrar nova pessoa', 'Listar pessoas cadastradas', 'Deletar arquivo', 'Sair do programa'])
    if op == 1:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(1)
    elif op == 2:
        lerArquivo(arq)
        sleep(1)
    elif op == 3:
        cabeçalho('Excluindo programa')
        sleep(2)
        apagarArquivo(arq)
    elif op == 4:
        cabeçalho('Saindo do programa')
        for c in range(0, 4):
            print('.', end='', flush=True)
            sleep(0.6)
        print('\nAté breve!')
        break

