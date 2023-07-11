numi = int(input('Digite um número inteiro: '))
print('''Agora escolha a base de conversão que deseja:
[ 1 ]Converter para BINÁRIO
[ 2 ]Converter para OCTAL
[ 3 ]Converter para HEXADECIMAL''')
conv = int(input('Digite sua opção:'))
if conv == 1:
    print('O numero {} convertido para BINÁRIO é igual a {}'.format(numi, bin(conv)[2:]))
elif conv == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(numi, oct(conv)[2:]))
else:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(numi, hex(conv)[2:]))