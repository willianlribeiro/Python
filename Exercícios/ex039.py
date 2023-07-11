from datetime import date
aniversario = int(input('Quanto tempo falta pra se alistar? Coloque aqui sua idade (XXXX) e saiba :'))
idade = date.today().year - aniversario
tempo = 18 - idade
if idade < 18:
    print('Ainda não chegou a data, mas fique em alerta, restam apenas {} anos pra você ter que se apresentar'.format(tempo))
elif idade == 18:
    print('Esse ano você precisa se alistar. Fique atento aos prazos para alistamento!')
else:
    print('A idade pra se alistar já passou {} anos, espero que esteja tudo em ordem'.format(tempo))