import random
import time
opcao = 0
print('Digite 2 valores e escolha uma das opções')
v1 = int(input('Valor número 1: '))
v2 = int(input('Valor número 2: '))
while opcao != 5:
    print('=-=-=-=-=-=-=-=-=-=\n[1]Somar\n[2]Multiplicar\n[3]Mostrar maior\n[4]Novos números\n[5]Sair do programa\n=-=-=-=-=-=-=-=-=-=')
    opcao = int(input('Digite qual opção escolheu'))
    if opcao == 1:
        print(v1 + v2)
        time.sleep(2)
    elif opcao == 2:
        print(v1 * v2)
        time.sleep(2)
    elif opcao == 3:
        if v1 > v2:
            print('O maior valor é {}'.format(v1))
        if v2 > v1:
            print('O maior valor é {}'.format(v2))
        else:
            print('Os valores são iguais')
        time.sleep(2)
    elif opcao == 4:
        v1 = int(input('Novo valor número 1: '))
        v2 = int(input('Novo valor número 2: '))
        print('Os valores agora são são {} e {}'.format(v1, v2))
        time.sleep(2)
    elif opcao == 5:
        print('Entendido, ', end='')
    else:
        print('Opção inválida, tente novamente')
        time.sleep(1)
print('desligando...')
time.sleep(3)
print('Obrigado por utilizar meu programa.')
time.sleep(1)
print('Até logo!')