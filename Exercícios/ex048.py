print('Soma entre todos os número ímpares entre 0-500 multiplos de 3')
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print(s)