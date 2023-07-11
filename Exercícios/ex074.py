from random import randint

tupla = tuple(randint(i + 1, 9) for i in range(1, 6))
menor = 0
maior = 0
print(f'Os números sorteados foram {tupla}')
print(f'O maior número gerado foi {max(tupla)}')
print(f'O menor número gerado foi {min(tupla)}')
