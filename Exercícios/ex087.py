matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
somacol = 0
maiorlin = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para posição {l}, {c}'))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            somacol += matriz[l][c]
        if matriz[1][c] == matriz[1][0]:
            maiorlin = matriz[1][0]
        if matriz[1][c] > maiorlin:
            maiorlin = matriz[1][c]
print('=#' * 11)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=#' * 11)
print(f'A soma dos valores pares é igual a: {somapar}')
print(f'A soma dos valores da terceira coluna é: {somacol}')
print(f'O maior número da segunda linha é: {maiorlin}')
