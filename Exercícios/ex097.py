def escreva(msg):
    for l in msg:
        print('~', end='')
    print()
    print(msg)
    for l in msg:
        print('~', end='')


#Projeto pricipal
mensagem = str(input('Digite aqui sua mensagem'))
escreva(mensagem)