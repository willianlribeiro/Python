from ex109 import moeda

p = float(input('Digite um valor para utilizar o módulo criado'))
print(f'A metade de {p} é {moeda.metade(p, True)}')
print(f'O dobro de {p} é {moeda.dobro(p, True)}')
print(f'Com acrecimo de 10% {p} fica {moeda.aumentar(p, 100, True)}')
print(f'Com desconto de 10% {p} fica {moeda.diminuir(p, 10, False)}')
