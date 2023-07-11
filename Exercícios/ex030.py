numero = int(input('Digite um numero e te direi se é par ou impar:'))
divi = numero%2
if divi == 1:
    print('{} é um número ÍMPAR'.format(numero))
else:
    print('{} é um número PAR'.format(numero))
