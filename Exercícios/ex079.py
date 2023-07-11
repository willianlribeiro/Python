lista = []
while True:
    numero = int(input('Adiocione aqui um número a sua lista'))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado')
    resposta = str(input('Deseja continuar ? S / N'))
    if resposta in 'Nn':
        break
lista.sort()
print('A lista criada ficou da seguinte forma \n'
      f'{lista}')