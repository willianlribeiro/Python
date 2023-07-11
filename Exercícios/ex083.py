expressão = str(input('Coloque aqui sua expressão para verificar se está correta.'))
parenteses = []
for elem in expressão:
    if elem == '(':
        parenteses.append('(')
    elif elem == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está errada.')

