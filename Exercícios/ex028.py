import random
adivinha = int(input('Tente adivinhar o numero que vou "pensar", entre 0 e 5:'))
escolhido = random.randrange(6)
if adivinha == escolhido:
    print('Parabéns, cagado')
else:
    print('KKKKKKKKKKK, EROUU')




