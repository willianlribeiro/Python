numeros = int(input('Digite números e eu direi a soma e quantos números foram digitados'))
contador = 1
soma = numeros
while True:
    numeros = int(input('Número: '))
    if numeros == 999:
        break
    contador += 1
    soma += numeros
print('Você digitou 999, o programa chegou ao fim!')
print(f'Foram digitados {contador} numeros e a soma entre eles foi de :{soma}.')
