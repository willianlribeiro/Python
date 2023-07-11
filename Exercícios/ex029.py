velocidade = int(input('Em qual velocidade você passou pelo radar?'))
multa = (velocidade - 80)*7
if velocidade <= 80:
    print('Você passou abaixo do limite de velocidade')
else:
    print('Você foi multado cara. Sifudeu! A multa custará um valor total de R${}'.format(multa))
8