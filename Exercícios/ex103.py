def formulario(a=0, b='<desconhecido>'):
    print(f'O jogador {b} fez {a} gol(s) no campeonato')


jog = str(input('Nome do jogador'))
gols = str(input('Quantos gol fez no campeonato'))
if gols.isnumeric():
    gols = int(gols)
else:
    a = 0
if jog.strip() == '':
    formulario(a=gols)
else:
    formulario(gols, jog)