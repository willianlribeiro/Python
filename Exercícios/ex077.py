tupla = ('borracha', 'apontador', 'lapiseira', 'biblia', 'caneta', 'abelha', 'dktydkyrd', 'flor', 'kfer', 'seila')
for palavra in tupla:
    print(f'\n A palavra #{palavra}# contém :', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f' {letra}', end='')


