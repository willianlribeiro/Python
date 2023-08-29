def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha():
            print(f'::Error:: o valor "{msg}" informado não é um número')
        else:
            valido = True
            return float(entrada)

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
