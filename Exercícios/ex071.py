print('Banco do Willian')
valor = int(input('Quanto gostaria de sacar da sua conta?'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        totced += 1
        total -= ced
    else:
        if ced == 50:
            ced = 20
            


print(f'O valor sera sacado num total de {n50} cédulas de R$50')
print(f'{n20} cédulas de R$20')
print(f'{n10} cédulas de R$10')
print(f'{n1} cédulas de R$1')