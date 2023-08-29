from random import randint
from time import sleep
from operator import itemgetter
print(f'Valores sorteados:')
ranking = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
for k, v in ranking.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1.5)
geral = sorted(ranking.items(), key=itemgetter(1), reverse=True)
print('A classificação ficou:')
for i, l in enumerate(geral):
    print(f'Em {i+1} lugar,{l[0]} com {l[1]} pontos')
    sleep(1)
