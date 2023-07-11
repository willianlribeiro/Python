print('Vamos jogar par ou impar?')
import random
contador = 0
while True:
    valor = int(input('Diga um valor:'))
    escolha = str(input('P para PAR /// I para IMPAR')).lower().strip()
    pcpick = random.randint(0, 10)
    valor2 = valor + pcpick
    if valor2 % 2 == 1 and escolha == 'i':
        print(f'Parabéns {valor2} é IMPAR, você venceu')
        contador += 1
    elif valor2 % 2 == 0 and escolha == 'p':
        print(f'Parabéns {valor2} é PAR, você venceu')
        contador += 1
    else:
        print(f'Você perdeu. Eu escolhi {pcpick} e a soma foi {valor2}')
        break
print(f'Tente novamente. Você venceu {contador} vezes')

