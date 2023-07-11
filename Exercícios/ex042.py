print('Digite o valor de 3 retas e te direi se é possivel formar um triangulo com elas e qual triangulo é.')
r1 = float(input('Primeira'))
r2 = float(input('Segunda'))
r3 = float(input('Terceira'))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('É possível formar um triangulo com estes segmentos de reta. O triangulo é :', end='')
    if r1 == r2 == r3:
        print(' EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO')
    else:
        print(' ISOSCELE')
else:
    print('Não é possível formar um triangulo')