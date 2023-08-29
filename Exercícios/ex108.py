from ex108 import moeda

p = float(input('Digite um valor para utilizar o módulo criado'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Com acrecimo de 10% {moeda.moeda(p)} fica {moeda.moeda(moeda.aumentar(p, 100))}')
print(f'Com desconto de 10% {moeda.moeda(p)} fica {moeda.moeda(moeda.diminuir(p, 10))}')
