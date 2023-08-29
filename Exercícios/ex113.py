def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Oops.. você não digitou um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar o valor')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Oops.. você não digitou um número real válido')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar o valor')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número inteiro')
n2 = leiaFloat('Digite um número real')
print(f'O valor inteiro digitado foi {n1} e real {n2}')


