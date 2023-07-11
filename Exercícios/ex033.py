print('Coloque 3 números e eu direi a ordem deles')
n1 = int(input('Número 1 : '))
n2 = int(input('Número 2 : '))
n3 = int(input('Numero 3 : '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('{} é o maior número. E o menor é {}'.format(maior, menor))