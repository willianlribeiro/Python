preco = float(input('Quer saber o valor com desconto? Coloque o preço do produto'))
desc = preco*0.05
precocdesc = preco*0.95
print('O valor do desconto fica {:.2f}, totalizando {:.2f} '.format(desc, precocdesc))