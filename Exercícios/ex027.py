nome = str(input('Coloque seu nome completo')).lower().strip()
spnome = nome.split()
print('Nome completo {}'.format(nome))
print('Priemiro nome: {}'.format(spnome[0]))
print('Ultimo nome: {}'.format(spnome[len(spnome)-1]))

