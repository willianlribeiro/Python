print('\033[35;40mBora calcular sua média? preencha os campos com suas notas\033[m')
nota1 = float(input('Qual foi sua primeira nota?'))
nota2 = float(input('Qual foi sua segunda nota?'))
media = (nota1 + nota2)/2
if media <= 5:
    print('Sua média foi {:.2f}. Infelizmente você não atingiu a média necessária. Estude mais'.format(media))
elif media > 5 and media <= 7:
    print('Sua média foi {:.2f}. Você está de recuperação.'.format(media))
else:
    print('\033[42mParabéns, você passou! Sua média foi {}\033[m'.format(media))