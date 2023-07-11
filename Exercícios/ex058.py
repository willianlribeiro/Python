import random
escolhido = random.randrange(0, 11)
contador = 0
adivinha = int(input('Tente adivinhar o numero que vou "pensar", entre 0 e 10:'))
while adivinha != escolhido:
    print('Você não acertou, continue tentando')
    adivinha = int(input('Tente adivinhar o numero que vou "pensar", entre 0 e 10:'))
    contador += 1
print('Parabéns, você levou {}x para acertar o número que pensei.'.format(contador))