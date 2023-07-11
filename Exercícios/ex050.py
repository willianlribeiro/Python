print('Digite 6 números inteiros e eu irei somar somente aqueles que forem pares')
soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('número {} : '.format(c)))
    if n1 % 2 == 0:
        soma += n1
        cont += 1
print('Foram contados {} numeros pares e a soma entre eles foi de {}'.format(cont, soma))



