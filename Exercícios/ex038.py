numero1 = int(input('\033[7mCologue dois números e eu direi qual deles é maior :\033[m'))
numero2 = int(input('\033[7mSegundo número :\033[m'))
if numero1 > numero2:
    print('O primeiro número é maior que o segundo número')
elif numero2 > numero1:
    print('O segundo número é maior que o primeiro número')
elif numero1 == numero2:
    print('Os números escolhidos são iguais')