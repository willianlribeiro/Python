print('Bem-vindo a nossa loja!')
resposta = ' '
produtoscar = 0
total = 0
nomeb = ' '
maisbarato = 0
while resposta != 'n':
    nomes = str(input('Qual o nome do produto escolhido?'))
    produtos = int(input('Preço do produto:'))
    total += produtos
    maisbarato = produtos
    if produtos > 1000:
        produtoscar += 1
    elif produtos <= maisbarato:
        nomeb = nomes
    resposta = str(input('Deseja continuar ? [\033[1;32;40mS\033[m / \033[1;31;40mN\033[m]')).lower().strip()
print(f'O total gasto na compra foi de {total}.')
print(f'{produtoscar} produto(s) custou(aram) mais de R$1.000 reais')
print(f'O nome do produto mais barato é {nomeb}')

