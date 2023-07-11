import random
print('Bora jogar Jokenpô?')
ppick = str(input('Escolha entre pedra, tesoura ou papel e digite aqui').lower())
jkp = ['pedra', 'tesoura', 'papel']
pcpick = random.choice(jkp)
if ppick == 'tesoura' and pcpick == 'papael':
    print('Parabéns, você ganhou! Eu tinha escolhido {}.'.format(pcpick))
elif ppick == 'pedra' and pcpick == 'tesoura':
    print('Parabéns, você ganhou! Eu tinha escolhido {}.'.format(pcpick))
elif ppick == 'papel' and pcpick == 'pedra':
    print('Parabéns, você ganhou! Eu tinha escolhido {}.'.format(pcpick))
elif ppick == pcpick:
    print('Você olhou, eu também tinha escolhido {}.'.format(ppick))
elif ppick != 'pedra' and ppick != 'papel' and ppick != 'tesoura':
    print('Você digitou algo errado ou "mingou". Então eu ganhei...')
else:
    print('Que pena, você escolheu {} e eu {}. {} ganha de {}.'.format(ppick, pcpick, pcpick, ppick))