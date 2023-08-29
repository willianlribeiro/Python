def leiaint(numero=''):
    while True:
        numero = str(input('Digite o número'))
        if numero.isnumeric() == True:
            return numero
        else:
            print('\033[1:31:40m Erro, digite um número válido \033[m')


numero = leiaint
print(f'O número digitado foi {leiaint(numero)}')
