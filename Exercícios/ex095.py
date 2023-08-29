tabela = []
jogador = {}
while True:
    jogador.clear()
    saldo = 0
    gols = []
    jogador['Nome'] = str(input('Nome do jogador'))
    jogador['Partidas'] = int(input(f'Quantas partidas no campeonato {jogador["Nome"]} teve?'))
    for p in range(0, jogador['Partidas']):
        gols.append(int(input(f'Quantos gols na partida {p+1}?')))
    for g, s in enumerate(gols):
        saldo += s
    jogador['Aproveitamento'] = gols
    jogador['Saldo'] = saldo
    tabela.append(jogador.copy())
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'nN':
        break
print('=-'*20)
print(tabela)
for it in jogador.keys():
    print(f'{it:<15}', end='')
print()
for k, v in enumerate(tabela):
    print(f'{k}', end='')
    print(f'{v["Nome"]:>6}       {v["Aproveitamento"]} {v["Saldo"]:>23}')