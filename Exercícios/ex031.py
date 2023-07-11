viagem = int(input('Qual a distância da sua viagem?Irei calcular seus gastos...'))
viageml = viagem*0.45
viagemc = viagem*0.50
if viagem >= 200:
    print('Sua viagem custará R${}'.format(int(viageml)))
else:
    print('Sua viagem custará R${}'.format(int(viagemc)))