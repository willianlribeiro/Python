p = ('Lápis', 0.75, 'Borracha', 2.00, 'Apontador', 1.50,'Resma de papel', 23.00, 'Caderno', 10.30, 'Estojo', 5.50, 'Compasso', 3.50, 'Cartolina', 3.20, 'Caneta', 1.50, 'Giz', 6.00)
print('           Listagem de preços         ')
print('-='*23)
for iten in range(0, len(p)):
    if iten % 2 == 0:
        print(f'{p[iten]:.<35}', end='')
    else:
        print(f'R${p[iten]:>5}')
print('-='*23)