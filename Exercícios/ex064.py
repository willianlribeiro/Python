numeros = 0
somatorio = 0
contador = 0
numeros2 = 0
while numeros != 999:
    somatorio += numeros2
    numeros2 = int(input('Coloque vários números e digite 999 para parar o programa.'))
    numeros = numeros2
    contador += 1
print('Somando todos números digitados temos: {} e foram contados {} números.'.format(somatorio, contador - 1 ))
