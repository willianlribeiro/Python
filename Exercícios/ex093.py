jogador = {}
gols = []
saldo = 0
jogador['Nome'] = str(input('Nome do jogador'))
jogador['Partidas'] = int(input(f'Quantas partidas no campeonato {jogador["Nome"]} teve?'))
for p in range(0, jogador['Partidas']):
    gols.append(int(input(f'Quantos gols na partida {p+1}?')))
for g, s in enumerate(gols):
    saldo += s
jogador['Aproveitamento'] = gols
print(f"O nome do jogador é {jogador['Nome']}")
print(f"{jogador['Nome']} fez {jogador['Partidas']} partidas")
print(f"Teve um aproveitamento de {saldo} gols")
print(jogador)

