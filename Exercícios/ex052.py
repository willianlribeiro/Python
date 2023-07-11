print('Digite um número e eu irei dizer se ele é um numero primo ou não')
num = int(input('Número : '))
total = 0
for c in range(1, num+1, 1):
    if num % c == 0:
        print('\033[35m', end=' ')
        total += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end='')
if total == 2:
    print('\033[m \n{} é um número primo'.format(num))
else:
    print('\n {} não é um número primo'.format(num))