print('Digite números e eu direi quantos foram e a média entre eles')
pergunta = str(input('Adicionar números? [ S / N ]')).lower().strip()
numeros = int(input('Próximo numero:'))
maior = numeros
menor = numeros
somatorio = numeros
contador = 1
while pergunta != 'n':
    numeros = int(input('Próximo numero:'))
    somatorio += numeros
    contador += 1
    if numeros <= menor:
        menor = numeros
    elif numeros >= maior:
        maior = numeros
    pergunta = str(input('Adicionar números? [ S / N ]')).lower().strip()
media = somatorio / contador
print('A média dos números adicionados foi de {}. O maior número foi {} e o menor {}'.format(media, maior, menor))
