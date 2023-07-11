import math
numero = float(input('Digite algum número real'))
ared = math.ceil(numero)
aredm = math.floor(numero)
print('O numero arredondado pra baixo fica {} e pra cima {}'.format(aredm, ared))