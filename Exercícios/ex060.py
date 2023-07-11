from time import sleep
print('Digite um número e saiba seu fatorial')
num = int(input('Número :'))
f = 1
n = num
print('Calculando fatorial de {}...'.format(num))
sleep(2)
while n > 0:
    print('{} '.format(n), end='')
    print('x ' if n > 1 else '= ', end='')
    f *= n
    n -= 1
print('{}'.format(f))

