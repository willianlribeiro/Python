numero1 = (int(input('Digite um número')),
              int(input('Digite outro número')),
              int(input('Digite mais um número')),
              int(input('Digite o último número')))
print(f'O 9 aparece {numero1.count(9)} vezes')
if 3 in numero1:
    print(f'O número 3 apareceu na {numero1.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado nenhuma vez')
for n in numero1:
    if n % 2 == 0:
        print(f'O número {n} é par')

