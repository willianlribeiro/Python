from ex111.UtilidadeCeV import dado
from ex111.UtilidadeCeV import moeda


p = dado.leiaDinheiro('Digite o preço R$:')
print(moeda.resumo(p, 35, 22))
