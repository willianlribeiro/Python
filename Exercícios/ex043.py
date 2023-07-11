print('Vamos calcular seu IMC')
peso = int(input('Qual seu peso?'))
altura = float(input('Qual é sua altura?'))
imc = peso / altura**2
if imc <= 18.5:
    print('De acordo com seu IMC, você está abixo do peso')
elif imc > 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc > 25 and imc < 30:
    print('Sobrepeso')
elif imc > 30 and imc < 40:
    print('Você está obeso')
else:
    print('Cuidado!, de acordo com seu IMC você está com obesidade mórbida')