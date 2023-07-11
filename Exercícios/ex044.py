preco = float(input('Qual o preço do produto?'))
avd = preco - preco*0.10
avc = preco - preco*0.05
par3 = preco + preco*0.3
print('O produto no valor de R${:.2f}, fica R${:.2f} à vista no dinheiro.'.format(preco, avd))
print('R${:.2f} a vista no cartão.'.format(avc))
print('R${:.2f} parcelado em até 2x.'.format(preco))
print('ou R${:.2f} parcelado em 3x ou mais.'.format(par3))