numero = str(input('Coloque um número entre 0 e 9999'))
numerosep = numero.split()
uni = numero[3]
dez = numero[2]
cen = numero[1]
mil = numero[0]
print('Unidade: {}'.format(uni))
print('dezena: {}'.format(dez))
print('centena: {}'.format(cen))
print('milhar: {}'.format(mil))