print('Diga 5 pesos de pessoas diferentes e eu direi quem é o mais pesado e o mais leve')
maiorp = 0
menorp = 0
for c in range(1, 5+1):
    pesos = int(input('Digite aqui o peso da {} pessoa'.format(c)))
    if c == 1:
        maiorp = pesos
        menorp = pesos
    else:
        if pesos >= maiorp:
            maiorp = pesos
        if pesos <= menorp:
            menorp = pesos
print('O maior peso foi de {}Kg'.format(maiorp))
print('O menor peso foi de {}Kg'.format(menorp))
