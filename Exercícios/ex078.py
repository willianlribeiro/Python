lista = []
maior = 0
menor = 0
print('Digite 5 valores para criar uma lista')
for c in range(0, 5):
    lista.append(int(input('Digite aqui os valores ->')))
    menor = c
    if lista[c] > maior:
        maior = lista[c]
    if lista[c] < menor:
        menor = lista[c]
print(f'Você digitou os valores {lista}')
print(f'A posição do maior ({maior}) é {lista.index(maior)+1}ª posição e a do menor ({menor}) é a {lista.index(menor)+1}ª posição')