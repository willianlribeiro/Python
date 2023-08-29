def área(a, b):
    m = a * b
    print(f'A área do terreno, com as dimensões {a:.1f}x{b:.1f}, é {m:.1f}m²')


#Programa principal
largura = float(input(f'Digite o valor da largura'))
comprimento = float(input(f'Digite o valor da altura'))
área(largura, comprimento)

