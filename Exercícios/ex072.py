numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numerodig = int(input('Digite um valor entre 0 - 20 para saber como fica por extenso'))
while True:
    if numerodig < 0 or numerodig > 20:
        numerodig = int(input('Digite um valor válido entre 0 - 20'))
    else:
        break
print(f'O número digitado por extenso é {numero[numerodig]}')
