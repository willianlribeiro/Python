lista = [0]
for c in range(0, 5):
    n = int(input(f'Digite aqui o {c+1}ª valor'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('Sua lista ficou da seguinte forma\n'
      f'{lista}')