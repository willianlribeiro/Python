import datetime

from ex115.lib.interface import *
from datetime import time


def verificarArquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso!!')


def lerArquivo(nome):
    try:
        a = open(nome)
    except:
        print('Houve um erro ao tentar abrir o arquivo :/')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for pessoa in a:
            try:
                dado = pessoa.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30}{dado[1]:>3} anos')
            except:
                print('A lista provavelmente foi excluída')
                print(pessoa)
    finally:
        a.close()


def cadastrar(arq, nome='<Desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao tentar abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao tentar gravar no arquivo')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()


def apagarArquivo(nome):
    if verificarArquivo(nome) == True:
        a = open(nome, 'w')
        try:
            a.write(f'Arquivo anterior excluído em {datetime.date.today()} \n')
        finally:
            print(f'Arquivo {nome} excluído com sucesso')
            a.close()


